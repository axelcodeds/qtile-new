#!/bin/bash

# Aplicaciones que quieres iniciar
#nm-applet &      # Network Manager
#blueman-applet & # Bluetooth
picom &          # Compositor para efectos
#flameshot &      # Captura de pantalla
#redshift &       # Filtro de luz azul

xrandr --output Virtual1 --mode 1920x1080 --rate 60 &