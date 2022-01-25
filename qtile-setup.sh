sudo pacman -Syu --needed base-devel
git clone https://aur.archlinux.org/paru-bin.git
cd paru
makepkg -si

paru -S --noconfirm alacritty auto-cpufreq backlight_control bluez bluez-utils blueman btop cmatrix discord dunst figlet firefox-developer-edition fluent-gtk-theme-git fluent-cursor-theme-git github-desktop-bin gvfs htop i3lock-color imagemagick light lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings lolcat lollypop lxappearance maim moc multimc-bin mpv neofetch nerd-fonts-complete network-manager-applet nitrogen noto-fonts-emoji ntfs-3g pamixer pavucontrol picom-jonaburg-git polkit-gnome pulseaudio pulseaudio-alsa pulseaudio-bluetooth pulseaudio-jack python-dbus python-gobject qbittorrent-dark-git qogir-gtk-theme-git qtile refind rofi spotify stacer-git teams-for-linux touchegg touche tela-icon-theme-bin thunar ttf-unifont ttf-ms-fonts viewnior vscodium-bin whatsapp-nativefier-dark xclip xorg zoom

for service in bluetooth lightdm NetworkManager touchegg.service; do
  sudo systemctl enable --now $service
done

git clone https://github.com/Z-8Bit/Qtile.git ~/Downloads/Qtile

mkdir -p ~/.config/{alacritty,cava,dunst,qtile,rofi,neofetch,touchegg}

cp ~/Downloads/Qtile/qtile/config.py ~/.config/qtile/
cp ~/Downloads/Qtile/alacritty/alacritty.yml ~/.config/alacritty/
cp -r ~/Downloads/Qtile/dunst/* ~/.config/dunst/
cp ~/Downloads/Qtile/rofi/* ~/.config/rofi/
cp ~/Downloads/Qtile/touchegg/touchegg.conf ~/.config/touchegg/
cp ~/Downloads/Qtile/neofetch/config.conf ~/.config/neofetch/
cp ~/Downloads/Qtile/picom.conf ~/.config/

sudo systemctl start touchegg
cp ~/Downloads/Qtile/xprofile ~/.xprofile
cp ~/Downloads/Qtile/Xresources ~/.Xresources
chmod +x ~/Downloads/Qtile/scripts/*.sh
sudo cp ~/Downloads/Qtile/scripts/*.sh /usr/bin/
refind-install

git clone https://github.com/Z-8Bit/Wallpapers ~/Pictures/Wallpapers
RED='\033[0;31m'

sleep 5
echo -e "${RED}Please add ~/Pictures/Wallpapers in nitrogen's preferences"

sudo cp ~/Downloads/Qtile/lightdm-gtk-greeter.conf /etc/lightdm/
sudo cp ~/Pictures/Wallpapers/ARTWORK-wanderer-above-the-sea-of-fog.jpg /etc/lightdm/

# sudo pacman -S refind && refind-install
# git clone https://github.com/josephsurin/refind-theme-circle.git && sudo rm -r ./refind-theme-circle/{screenshots,.git}
# sudo cp -r refind-theme-circle /boot/efi/EFI/refind/ && sudo echo "include refind-theme-circle/theme.conf" >> /boot/efi/EFI/refind/refind.conf

sleep 5
echo -e "${RED}PLEASE REBOOT NOW"



