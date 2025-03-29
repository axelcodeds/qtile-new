class Colors:
    # Esquema Dracula (popular para desarrollo)
    DRACULA = {
        'background': '#282a36',
        'foreground': '#f8f8f2',
        'primary': '#bd93f9',
        'secondary': '#ff79c6',
        'alert': '#ff5555',
        'warning': '#f1fa8c',
        'success': '#50fa7b',
        'inactive': '#6272a4',
        'active': '#ff79c6'
    }

    # Esquema Nord (colores fríos)
    NORD = {
        'background': '#2e3440',
        'foreground': '#d8dee9',
        'primary': '#81a1c1',
        'secondary': '#5e81ac',
        'alert': '#bf616a',
        'warning': '#ebcb8b',
        'success': '#a3be8c',
        'inactive': '#4c566a',
        'active': '#88c0d0'
    }

    # Esquema Solarized Dark
    SOLARIZED_DARK = {
        'background': '#002b36',
        'foreground': '#839496',
        'primary': '#268bd2',
        'secondary': '#2aa198',
        'alert': '#dc322f',
        'warning': '#b58900',
        'success': '#859900',
        'inactive': '#586e75',
        'active': '#93a1a1'
    }

    # Esquema personalizado (modifícalo a tu gusto)
    CUSTOM = {
        'background': '#1a1b26',       # Fondo oscuro
        'foreground': '#a9b1d6',       # Texto principal
        'primary': '#7aa2f7',          # Azul brillante
        'secondary': '#bb9af7',        # Morado
        'alert': '#f7768e',            # Rojo/rosa
        'warning': '#e0af68',          # Amarillo/naranja
        'success': '#9ece6a',          # Verde
        'inactive': '#565f89',         # Elementos inactivos
        'active': '#7dcfff'            # Elementos activos
    }

# Selecciona el esquema de colores a usar (cambia DRACULA por tu preferencia)
current_theme = Colors.CUSTOM