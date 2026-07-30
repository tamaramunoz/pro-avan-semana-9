WINDOW_TITLE = "Sistema de Gestión de Flota - Agencia de Alquiler"
WINDOW_GEOMETRY = "780x660"
WINDOW_RESIZABLE = (False, False)

FONT_TITLE = ("Arial", 10, "bold")
FONT_BTN = ("Arial", 9, "bold")
COLOR_PRIMARY = "#1565C0"

FRAME_FORM_CONFIG = {
    "text": " Información del Vehículo ",
    "padx": 15,
    "pady": 10,
    "fg": COLOR_PRIMARY,
    "font": FONT_TITLE
}

FRAME_TABLE_CONFIG = {
    "text": " Flota de Vehículos Registrados ",
    "padx": 10,
    "pady": 10
}

BTN_ADD = {
    "bg": "#2E7D32",
    "fg": "black",
    "highlightbackground": "#2E7D32",
    "width": 13,
    "font": FONT_BTN
}

BTN_UPDATE = {
    "bg": COLOR_PRIMARY,
    "fg": "black",
    "highlightbackground": COLOR_PRIMARY,
    "width": 13,
    "font": FONT_BTN
}

BTN_DELETE = {
    "bg": "#C62828",
    "fg": "black",
    "highlightbackground": "#C62828",
    "width": 13,
    "font": FONT_BTN
}

BTN_CLEAR = {
    "bg": "#424242",
    "fg": "black",
    "highlightbackground": "#424242",
    "width": 13,
    "font": FONT_BTN
}

BTN_REPORT = {
    "bg": "#6A1B9A",
    "fg": "black",
    "highlightbackground": "#6A1B9A",
    "width": 13,
    "font": FONT_BTN
}

TABLE_COLUMNS = ("ID", "Marca", "Modelo", "Año", "Combustible", "Estado")

TABLE_COLUMN_CONFIGS = {
    "ID": {"width": 40, "anchor": "center"},
    "Marca": {"width": 120},
    "Modelo": {"width": 120},
    "Año": {"width": 70, "anchor": "center"},
    "Combustible": {"width": 110, "anchor": "center"},
    "Estado": {"width": 160, "anchor": "center"}
}