#!/bin/bash

# Ruta de la batería (puede variar, verifica en /sys/class/power_supply/)
BAT_PATH="/sys/class/power_supply/BAT0"

# Iconos según el porcentaje (Nerd Fonts)
ICON_LOW="󰁺"      # Menos del 20%
ICON_MID="󰁼"      # 20-50%
ICON_HIGH="󰂀"     # 50-80%
ICON_FULL="󰁹"     # 80-100%
ICON_CHARGING="󰂄" # Cuando está cargando

# Función para obtener el porcentaje
get_battery_percentage() {
    cat "${BAT_PATH}/capacity" 2>/dev/null || echo "0"
}

# Función para verificar si está cargando
is_charging() {
    grep -q "Charging" "${BAT_PATH}/status" 2>/dev/null
}

# Obtener datos
PERCENT=$(get_battery_percentage)

# Elegir ícono según el estado y nivel
if is_charging; then
    ICON="$ICON_CHARGING"
elif [ "$PERCENT" -lt 20 ]; then
    ICON="$ICON_LOW"
elif [ "$PERCENT" -lt 50 ]; then
    ICON="$ICON_MID"
elif [ "$PERCENT" -lt 80 ]; then
    ICON="$ICON_HIGH"
else
    ICON="$ICON_FULL"
fi

# Mostrar resultado (formato: 󰂄 50% o 󰁹 100%)
echo "${ICON} ${PERCENT}%"