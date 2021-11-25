sudo pacman -Syu --needed base-devel
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si

paru -S --noconfirm alacritty backlight_control cmatrix dunst figlet fluent-cursor-theme-git i3lock-color lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings lolcat lxappearance maim neofetch nerd-fonts-complete network-manager-applet nitrogen noto-fonts-emoji picom-jonaburg-git polkit-gnome pulseaudio pulseaudio-alsa pulseaudio-bluetooth python-dbus python-gobject qogir-gtk-theme-git qtile rofi tela-icon-theme thunar touchegg touche ttf-ms-fonts xclip xorg

for service in bluetooth lightdm NetworkManager touchegg.service; do
  sudo systemctl enable --now $service
done

git clone https://github.com/Z-8Bit/Qtile.git ~/Downloads/Qtile

mkdir -p ~/.config/{alacritty,cava,dunst,qtile,rofi,neofetch,touchegg}

cp ~/Downloads/Qtile/qtile/config.py ~/.config/qtile/
cp ~/Downloads/Qtile/alacritty/alacritty.yml ~/.config/alacritty/
cp ~/Downloads/Qtile/dunst/dunstrc ~/.config/dunst/
cp ~/Downloads/Qtile/rofi/* ~/.config/rofi/
cp ~/Downloads/Qtile/touchegg/touchegg.conf ~/.config/touchegg/
cp ~/Downloads/Qtile/neofetch/config.conf ~/.config/neofetch/
cp ~/Downloads/Qtile/picom.conf ~/.config/

sudo systemctl start touchegg
cp ~/Downloads/Qtile/xprofile ~/.xprofile
cp ~/Downloads/Qtile/Xresources ~/.Xresources
chmod +x ~/Downloads/Qtile/scripts/*.sh
sudo cp ~/Downloads/Qtile/scripts/*.sh /usr/bin/

sleep 5
RED='\033[0;31m'
echo -e  "${RED}PLEASE REBOOT NOW"



