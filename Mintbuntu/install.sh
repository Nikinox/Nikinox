#!/bin/bash

echo "======================================="
echo "        Mintbuntu Installer"
echo "   Transforming Lubuntu → XFCE"
echo "======================================="

sleep 1

echo " Updating packages..."
sudo apt update && sudo apt upgrade -y

echo " Installing XFCE..."
sudo apt install -y xfce4 xfce4-goodies

echo " Installing essential tools..."
sudo apt install -y libfuse2 xfce4-screenshooter file-roller

echo " Downloading XFCE configuration..."

TAR_URL="https://raw.githubusercontent.com/Nikinox/Mintbuntu/main/xfce-config.tar.gz"

wget -q "$TAR_URL" -O /tmp/xfce-config.tar.gz

if [ -f /tmp/xfce-config.tar.gz ]; then
    echo "Applying XFCE configuration..."
    tar -xzf /tmp/xfce-config.tar.gz -C ~/
else
    echo "WARNING: xfce-config.tar.gz not found or download failed!"
fi

echo " Setting workspace count to 1..."
xfconf-query -c xfwm4 -p /general/workspace_count -t int -s 1 --create

echo " Moving the panel to the bottom..."
xfconf-query -c xfce4-panel -p /panels/panel-1/position -t string -s "p=8;x=0;y=0" --create

echo " Configuring screenshot shortcuts..."
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/Print" -t string -s "xfce4-screenshooter" --create
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Shift>Print" -t string -s "xfce4-screenshooter -r" --create
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Alt>Print" -t string -s "xfce4-screenshooter -w" --create

echo " Applying dark terminal theme..."
xfconf-query -c xfce4-terminal -p /color-background -t string -s "#000000" --create
xfconf-query -c xfce4-terminal -p /color-foreground -t string -s "#FFFFFF" --create
xfconf-query -c xfce4-terminal -p /color-palette -t string -s \
"black:#000000;red:#CC0000;green:#4E9A06;yellow:#C4A000;blue:#3465A4;magenta:#75507B;cyan:#06989A;white:#D3D7CF;brightblack:#555753;brightred:#EF2929;brightgreen:#8AE234;brightyellow:#FCE94F;brightblue:#729FCF;brightmagenta:#AD7FA8;brightcyan:#34E2E2;brightwhite:#EEEEEC" --create
xfconf-query -c xfce4-terminal -p /use-system-theme -t bool -s false --create

echo ">>> Installing ZRAM and bpytop..."
sudo apt install -y util-linux zram-config bpytop

echo " Asking about disabling optional services..."

read -p "Disable Bluetooth service? (y/N): " ans
[[ $ans == "y" ]] && sudo systemctl disable --now bluetooth.service

read -p "Disable Avahi (network discovery)? (y/N): " ans
[[ $ans == "y" ]] && sudo systemctl disable --now avahi-daemon.service

read -p "Disable CUPS (printing)? (y/N): " ans
[[ $ans == "y" ]] && sudo systemctl disable --now cups.service

read -p "Disable ModemManager (4G dongles)? (y/N): " ans
[[ $ans == "y" ]] && sudo systemctl disable --now ModemManager.service

echo " Final cleanup before switching desktop..."
echo "XFCE fully installed and configured."

echo " Removing LXQt and Openbox..."
sudo apt remove --purge -y lxqt* openbox* obconf* pcmanfm-qt* lximage-qt*
sudo apt remove lxqt-archiver
sudo apt autoremove --purge -y

echo "LXQt removed. Rebooting now..."
sudo reboot
