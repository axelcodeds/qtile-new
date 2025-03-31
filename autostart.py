import os
import subprocess

def run_autostart():
    commands = [
        "xrandr --output Virtual1 --mode 1920x1080 --rate 60",
        "cbatticon -n",
        "feh --bg-fill ~/Pictures/wallpapers/01.jpg",  # Usar ~ para home
        "volumeicon",
        "nm-applet -n",
    ]
    
    for cmd in commands:
        try:
            # Usamos shell=True para manejar rutas con ~ y comandos complejos
            subprocess.Popen(cmd, shell=True)
        except Exception as e:
            print(f"Error al ejecutar '{cmd}': {e}")