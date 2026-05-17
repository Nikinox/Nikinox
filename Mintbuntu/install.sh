#!/bin/bash

echo "======================================="
echo "        Mintbuntu Installer"
echo "   transformation Lubuntu → XFCE"
echo "======================================="

sleep 1

echo "[1/9] updating packs..."
sudo apt update && sudo apt upgrade -y

echo "[2/9] Installing XFCE..."
sudo apt install -y xfce4 xfce4-goodies

echo "[3/9] Removing LXQt and Openbox..."
sudo apt remove --purge -y lxqt* openbox* obconf* pcmanfm-qt* lximage-qt*
sudo apt autoremove --purge -y

echo "[4/9] Installing essential tools..."
sudo apt install -y gdebi libfuse2 xfce4-screenshooter file-roller

echo "[5/9] recovering personalized XFCE configuration..."
if [ -f xfce-config.tar.gz ]; then
    tar -xzvf xfce-config.tar.gz -C ~/
    echo "Configurazione XFCE applicata."
else
    echo "  WARNING: xfce-config.tar.gz not founded!"
fi

echo "[6/9] leaving only one desktop space..."
xfconf-query -c xfwm4 -p /general/workspace_count -n -t int -s 1

echo "[7/9] moving the panel down..."
# Pannello principale = panel-1 (come nel tuo sistema)
xfconf-query -c xfce4-panel -p /panels/panel-1/position -n -t string -s "p=8;x=0;y=0"

echo "[8/9] Configuring screenshot shortcuts..."
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/Print" -n -t string -s "xfce4-screenshooter"
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Shift>Print" -n -t string -s "xfce4-screenshooter -r"
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Alt>Print" -n -t string -s "xfce4-screenshooter -w"

echo "[9/9] Applying dark terminal theme..."

# sets black background
xfconf-query -c xfce4-terminal -p /color-background -n -t string -s "#000000"

# sets white text
xfconf-query -c xfce4-terminal -p /color-foreground -n -t string -s "#FFFFFF"

# enables the style palette 'Linux'
xfconf-query -c xfce4-terminal -p /color-palette -n -t string -s "black:#000000;red:#CC0000;green:#4E9A06;yellow:#C4A000;blue:#3465A4;magenta:#75507B;cyan:#06989A;white:#D3D7CF;brightblack:#555753;brightred:#EF2929;brightgreen:#8AE234;brightyellow:#FCE94F;brightblue:#729FCF;brightmagenta:#AD7FA8;brightcyan:#34E2E2;brightwhite:#EEEEEC"

# Disables system theme (essential to get custom colors)
xfconf-query -c xfce4-terminal -p /use-system-theme -n -t bool -s false


echo "======================================="
echo " Mintbuntu succesfully installed!"
echo " Reboot to apply everything."
echo "======================================="
