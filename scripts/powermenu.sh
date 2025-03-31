#!/bin/bash
options="  Apagar\n  Reiniciar\n  Cerrar sesión"
selected=$(echo -e "$options" | rofi -dmenu -p "Menú de energía" -theme ~/.config/rofi/powermenu.rasi)

case "$selected" in
  "Apagar") systemctl poweroff ;;
  "Reiniciar") systemctl reboot ;;
  "Cerrar sesión") qtile cmd-obj -o cmd -f shutdown ;;
esac