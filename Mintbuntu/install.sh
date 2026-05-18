#!/bin/bash

echo "======================================="
echo "        Mintbuntu Installer"
echo "   Transforming Lubuntu → XFCE"
echo "======================================="

sleep 1

echo "[1/9] Updating packages..."
sudo apt update && sudo apt upgrade -y

echo "[2/9] Installing XFCE..."
sudo apt install -y xfce4 xfce4-goodies

echo "[3/9] Removing LXQt and Openbox..."
sudo apt remove --purge -y lxqt* openbox* obconf* pcmanfm-qt* lximage-qt*
sudo apt autoremove --purge -y

echo "[4/9] Installing essential tools..."
sudo apt install -y gdebi libfuse2 xfce4-screenshooter file-roller

echo "[5/9] Downloading XFCE configuration..."

TAR_URL="https://raw.githubusercontent.com/Nikinox/Mintbuntu/main/xfce-config.tar.gz"

wget -q "$TAR_URL" -O /tmp/xfce-config.tar.gz

if [ -f /tmp/xfce-config.tar.gz ]; then
    echo "Applying XFCE configuration..."
    tar -xzf /tmp/xfce-config.tar.gz -C ~/
else
    echo "WARNING: xfce-config.tar.gz not found or download failed!"
fi

echo "[6/9] Setting workspace count to 1..."
xfconf-query -c xfwm4 -p /general/workspace_count -t int -s 1 --create

echo "[7/9] Moving the panel to the bottom..."
# Only works if panel-1 exists (your config creates it)
xfconf-query -c xfce4-panel -p /panels/panel-1/position -t string -s "p=8;x=0;y=0" --create

echo "[8/9] Configuring screenshot shortcuts..."
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/Print" -t string -s "xfce4-screenshooter" --create
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Shift>Print" -t string -s "xfce4-screenshooter -r" --create
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Alt>Print" -t string -s "xfce4-screenshooter -w" --create

echo "[9/9] Applying dark terminal theme..."

# Background
xfconf-query -c xfce4-terminal -p /color-background -t string -s "#000000" --create

# Foreground
xfconf-query -c xfce4-terminal -p /color-foreground -t string -s "#FFFFFF" --create

# Linux palette (correct format)
xfconf-query -c xfce4-terminal -p /color-palette -t string -s \
"black:#000000;red:#CC0000;green:#4E9A06;yellow:#C4A000;blue:#3465A4;magenta:#75507B;cyan:#06989A;white:#D3D7CF;brightblack:#555753;brightred:#EF2929;brightgreen:#8AE234;brightyellow:#FCE94F;brightblue:#729FCF;brightmagenta:#AD7FA8;brightcyan:#34E2E2;brightwhite:#EEEEEC" --create

# Disable system theme
xfconf-query -c xfce4-terminal -p /use-system-theme -t bool -s false --create

echo "======================================="
echo " Mintbuntu successfully installed!"
echo " Reboot to apply everything."
echo "======================================="
