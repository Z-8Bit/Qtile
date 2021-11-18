sudo pacman -Syu --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

paru -S --noconfirm alacritty auto-cpufreq backlight_control bluez bluez-utils btop cmatrix discord dunst figlet firefox-developer-edition fluent-cursor-theme-git i3lock-color imagemagick lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings lolcat lollypop lxappearance maim mpv neofetch nerd-fonts-complete network-manager-applet nitrogen noto-fonts-emoji pavucontrol picom-jonaburg-git pulseaudio pulseaudio-alsa pulseaudio-bluetooth pulseaudio-jack python-dbus python-gobject qbittorrent-dark-git qogir-gtk-theme-git qtile refind rofi spotify stacer-git teams-for-linux touchegg touche tela-icon-theme thunar ttf-unifont ttf-ms-fonts viewnior vscodium-bin whatsapp-nativefier-dark xclip xorg zoom

for service in bluetooth lightdm NetworkManager touchegg.service; do
  sudo systemctl enable --now $service
done

git clone https://github.com/Z-8Bit/Qtile.git ~/Downloads/Qtile

mkdir -p ~/.config/{alacritty,cava,dunst,qtile,rofi,neofetch}

cp ~/Downloads/Qtile/qtile/config.py ~/.config/qtile/
cp ~/Downloads/Qtile/alacritty/alacritty.yml ~/.config/alacritty/
cp ~/Downloads/Qtile/dunst/dunstrc ~/.config/dunst/
cp ~/Downloads/Qtile/rofi/* ~/.config/rofi/
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

sleep 5
echo -e "${RED}PLEASE REBOOT NOW"



