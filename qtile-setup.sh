sudo pacman -Syu --needed base-devel
git clone https://aur.archlinux.org/paru-bin.git
cd paru-bin && makepkg -si

paru -S --noconfirm alacritty alsa-tools alsa-utils  backlight_control blueman bluez bluez-utils btop dbus-python discord dunst firefox-developer-edition fluent-cursor-theme-git fluent-gtk-theme-git github-desktop-bin gnome-screenshot gparted gvfs htop jdk-temurin light lightdm lightdm-gtk-greeter lollypop lxappearance maim microsoft-edge-stable-bin moc mpv multimc-bin neofetch nerd-fonts-jetbrains-mono network-manager-applet nitrogen noto-fonts-emoji ntfs-3g pamixer pavucontrol picom-jonaburg-git polkit-gnome powertop pulseaudio pulseaudio-alsa pulseaudio-bluetoothp ulseaudio-jack python-gobject qbittorrent-dark-git qogir-gtk-theme-git qtile refind rofi spotify spotify-adblock teams-for-linux tela-icon-theme thunar touche touchegg transmission-gtk ttf-ms-fonts ttf-unifont viewnior vscodium-bin whatsapp-nativefier-dark xclip xorg zoom zsh 

for serfievice in bluetooth NetworkManager touchegg.service; do
  sudo systemctl enable --now $service
done

git clone https://github.com/Z-8Bit/Qtile.git ~/Downloads/Qtile

mkdir -p ~/.config/{alacritty,cava,dunst,qtile,moc,rofi,neofetch,touchegg}

cp ~/Downloads/Qtile/qtile/config.py ~/.config/qtile/
cp ~/Downloads/Qtile/alacritty/alacritty.yml ~/.config/alacritty/
cp -r ~/Downloads/Qtile/dunst/* ~/.config/dunst/
cp ~/Downloads/Qtile/rofi/* ~/.config/rofi/
cp ~/Downloads/Qtile/touchegg/touchegg.conf ~/.config/touchegg/
cp ~/Downloads/Qtile/neofetch/config.conf ~/.config/neofetch/
cp ~/Downloads/Qtile/picom.conf ~/.config/
cp -r ~/Downloads/Qtile/moc/* ~/.config/moc/

sudo systemctl start touchegg
cp ~/Downloads/Qtile/xprofile ~/.xprofile
cp ~/Downloads/Qtile/Xresources ~/.Xresources
chmod +x ~/Downloads/Qtile/scripts/*.sh
sudo cp ~/Downloads/Qtile/scripts/*.sh /usr/bin/
sudo cp ~/Downloads/Qtile/30-touchpad.conf /etc/X11/xorg.conf.d
refind-install

git clone https://github.com/Z-8Bit/Wallpapers ~/Pictures/Wallpapers
RED='\033[0;31m'

sleep 5
echo -e "${RED}Please add ~/Pictures/Wallpapers in nitrogen's preferences"

sudo cp ~/Downloads/Qtile/lightdm-gtk-greeter.conf /etc/lightdm/
sudo cp ~/Pictures/Wallpapers/ARTWORK-wanderer-above-the-sea-of-fog.jpg /etc/lightdm/

# refind-install
# git clone https://github.com/josephsurin/refind-theme-circle.git && sudo rm -r ./refind-theme-circle/{screenshots,.git}
# sudo cp -r refind-theme-circle /boot/efi/EFI/refind/ && sudo echo "include refind-theme-circle/theme.conf" >> /boot/efi/EFI/refind/refind.conf

echo -e "{$RED}Reboot now and then enable lightdm (sudo systemctl enable lightdm.service)"



