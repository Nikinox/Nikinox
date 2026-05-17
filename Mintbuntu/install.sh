#!/bin/bash

echo "======================================="
echo "        Mintbuntu Installer"
echo "   transformation Lubuntu → XFCE"
echo "======================================="

sleep 1

echo "[1/8] updating packs..."
sudo apt update && sudo apt upgrade -y

echo "[2/8] Installing XFCE..."
sudo apt install -y xfce4 xfce4-goodies

echo "[3/8] Removing LXQt and Openbox..."
sudo apt remove --purge -y lxqt* openbox* obconf* pcmanfm-qt* lximage-qt*
sudo apt autoremove --purge -y

echo "[4/8] Installing essential tools..."
sudo apt install -y gdebi libfuse2 xfce4-screenshooter file-roller

echo "[5/8] recovering personalized XFCE configuration..."
if [ -f xfce-config.tar.gz ]; then
    tar -xzvf xfce-config.tar.gz -C ~/
    echo "Configurazione XFCE applicata."
else
    echo "  WARNING: xfce-config.tar.gz not founded!"
fi

echo "[6/8] leaving only one desktop space..."
xfconf-query -c xfwm4 -p /general/workspace_count -n -t int -s 1

echo "[7/8] moving the panel down..."
# Pannello principale = panel-1 (come nel tuo sistema)
xfconf-query -c xfce4-panel -p /panels/panel-1/position -n -t string -s "p=8;x=0;y=0"

echo "[8/8] Configuring screenshot shortcuts..."
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/Print" -n -t string -s "xfce4-screenshooter"
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Shift>Print" -n -t string -s "xfce4-screenshooter -r"
xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom/<Alt>Print" -n -t string -s "xfce4-screenshooter -w"

echo "======================================="
echo " Mintbuntu succesfully installed!"
echo " Reboot to apply everything."
echo "======================================="
