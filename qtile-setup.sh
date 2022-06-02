sudo pacman -Syu --needed base-devel
git clone https://aur.archlinux.org/paru-bin.git
cd paru-bin && makepkg -si

sudo timedatectl set-ntp true && sudo timedatectl set-local-rtc 1 --adjust-system-clock

# Installing packages
paru -S --noconfirm alacritty alsa-tools alsa-utils audacious-plugins-gtk3 audacious-gtk3 brillo blueman bluez bluez-utils btop dbus-python discord dunst firefox-developer-edition fluent-cursor-theme-git fluent-gtk-theme-git github-desktop-bin gnome-screenshot gparted gvfs htop jdk-temurin light lightdm lightdm-gtk-greeter lxappearance maim mesa moc mpv multimc-bin neofetch nerd-fonts-jetbrains-mono network-manager-applet nitrogen noto-fonts-emoji ntfs-3g pamixer pavucontrol pipewire pipewire-alsa pipewire-pulse picom polkit-gnome powertop python-gobject polybar qtile refind rofi spotify spotify-adblock tar tela-icon-theme thunar touche touchegg transmission-gtk ttf-ms-fonts ttf-unifont unzip viewnior vscodium-bin whatsapp-nativefier-dark xclip xorg yt-dlg zip zoom zsh 

for service in bluetooth NetworkManager touchegg.service; do
  sudo systemctl enable --now $service
done

git clone https://github.com/Z-8Bit/Qtile.git ~/Downloads/Qtile

# Creating directories
mkdir -p ~/.config/{alacritty,audacious,dunst,moc,neofetch,polybar,qtile,rofi,touchegg}
# Making Thunar default file manager
xdg-mime default thunar.desktop inode/directory

# Copying dotfiles
cp ~/Downloads/Qtile/qtile/config.py ~/.config/qtile/
cp ~/Downloads/Qtile/alacritty/alacritty.yml ~/.config/alacritty/
cp -r ~/Downloads/Qtile/dunst/* ~/.config/dunst/
cp ~/Downloads/Qtile/rofi/* ~/.config/rofi/
cp ~/Downloads/Qtile/touchegg/touchegg.conf ~/.config/touchegg/
cp ~/Downloads/Qtile/neofetch/config.conf ~/.config/neofetch/
cp ~/Downloads/Qtile/misc/picom.conf ~/.config/
cp ~/Downloads/Qtile/moc/* ~/.config/moc/

# Scripts and Miscellaneous
chmod +x ~/Downloads/Qtile/scripts/*.sh
sudo cp ~/Downloads/Qtile/scripts/*.sh /usr/bin/
sudo cp ~/Downloads/Qtile/misc/30-touchpad.conf /etc/X11/xorg.conf.d
cp ~/Downloads/Qtile/misc/xprofile ~/.xprofile
cp ~/Downloads/Qtile/misc/Xresources ~/.Xresources

git clone https://github.com/Z-8Bit/Wallpapers ~/Pictures/Wallpapers
RED='\033[0;31m'

sleep 5
echo -e "${RED}Please add ~/Pictures/Wallpapers in nitrogen's preferences."

sudo cp ~/Downloads/Qtile/misc/lightdm-gtk-greeter.conf /etc/lightdm/
sudo cp ~/Pictures/Wallpapers/artwork.jpg /etc/lightdm/background.jpg

# Refind theming and installation
# refind-install
# git clone https://github.com/josephsurin/refind-theme-circle.git && sudo rm -r ./refind-theme-circle/{screenshots,.git}
# sudo cp -r refind-theme-circle /boot/efi/EFI/refind/ && sudo echo "include refind-theme-circle/theme.conf" >> /boot/efi/EFI/refind/refind.conf

echo -e "{$RED}Reboot now and then enable lightdm (sudo systemctl enable lightdm.service)."



