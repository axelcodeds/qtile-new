#!/bin/bash
terminal="alacritty"  # Cambia a tu terminal favorita

# Forzamos propiedades especiales para la ventana
$terminal --class=sysupdate \
          --title="Actualizador del Sistema" \
          -e bash -c \
          "echo '=== ACTUALIZANDO SISTEMA ==='; 
           sudo pacman -Syu; 
           echo; 
           read -p 'Actualización completada. Presiona Enter para salir...'; 
           exit"