#!/bin/bash

echo "Installing emojis..."
sudo apt install gnome-characters
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Super_L>period" -n -t string -s "gnome-characters"

echo "installing the searchbar for files..."
sudo apt install catfish

echo "installing and setting up ZRAM..."
sudo apt install zram-config
sudo systemctl enable --now zram-config

echo "installing all the tools..."
sudo apt install flatpak -y
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo apt install gimp vlc podman distrobox balena-etcher
flatpak install -y flathub io.github.dvlv.boxbuddy
sudo apt install neofetch xournalpp bpytop psensor
wget https://desktop.turbowarp.org/deb/turbowarp-desktop_latest_amd64.deb -O turbowarp.deb
sudo apt install ./turbowarp.deb -ys
pip install sounddevice pynput --break-system-packages


wget https://github.com/marktext/marktext/releases/latest/download/marktext-amd64.deb
sudo dpkg -i --verbose marktext-amd64.deb

echo "setting up VS code..."
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main"
sudo apt update
sudo apt install code
sudo apt install build-essential python3-tk python3-numpy
code --install-extension ms-vscode.cpptools
code --install-extension ms-python.python
code --install-extension formulahendry.code-runner

echo "setting up firefox..."
PROFILE=$(ls ~/.mozilla/firefox | grep default-release)
cat <<EOF > ~/.mozilla/firefox/$PROFILE/user.js
user_pref("toolkit.cosmeticAnimations.enabled", false);
user_pref("browser.tabs.animate", false);
user_pref("browser.fullscreen.animateUp", 0);
user_pref("browser.cache.memory.capacity", 51200);
user_pref("browser.cache.disk.enable", false);
user_pref("image.mem.decode_bytes_at_a_time", 32768);
user_pref("toolkit.telemetry.enabled", false);
user_pref("toolkit.telemetry.unified", false);
user_pref("browser.newtabpage.activity-stream.feeds.telemetry", false);
user_pref("browser.newtabpage.activity-stream.telemetry", false);
user_pref("general.smoothScroll", false);
user_pref("mousewheel.min_line_scroll_amount", 25);
EOF

echo "setting shortcuts..."
xfconf-query -c xfce4-keyboard-shortcuts \
  -p "/commands/custom/<Control><Alt>z" \
  -n -t string -s "psensor"
xfconf-query -c xfce4-keyboard-shortcuts \
  -p "/commands/custom/<Control><Shift>z" \
  -n -t string -s "xfce4-taskmanager"
xfconf-query -c xfce4-keyboard-shortcuts \
  -p "/commands/custom/<Super>." \
  -n -t string -s "gnome-characters"
xfconf-query -c xfce4-keyboard-shortcuts \
  -p "/commands/custom/<Super>r" \
  -n -t string -s "catfish"
xfconf-query -c xfce4-keyboard-shortcuts \
  -p "/commands/custom/<Super>e" \
  -n -t string -s "thunar"
xfconf-query -c xfce4-keyboard-shortcuts \
  -p "/commands/custom/<Control>p" \
  -n -t string -s "xfce4-terminal -e python3"

echo "setting the window's theme to Dark..."
xfconf-query -c xsettings -p /Net/ThemeName -s "Mint-Y-Dark"
xfconf-query -c xfwm4 -p /general/theme -s "Mint-Y-Dark"
xfce4-panel -r

echo "removing the useless stuff..."
sudo apt remove hypnotix gnome-calendar sticky simple-scan
sudo apt remove pix mint-meta-codecs thingy xfce4-dict system-config-printer mintchat
sudo apt remove fingwit

echo "setup completed successfully"
