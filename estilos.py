import json
import os
from pathlib import Path
#------------------TEMA---------------------------
configuracion = Path("json\\configuracion.json")

with open(configuracion, "r") as f: 
    data = json.load(f)
    tema_ruta = data["TEMA_SELECCIONADO"]
    if "\\" in tema_ruta: 
        ruta = tema_ruta
        with open (ruta, "r") as file:
            tema_data = json.load(file)

        tema_botones_color = tema_data["CTkButton"]["fg_color"]
        tema_frame_color =tema_data["CTkFrame"]["fg_color"]
        tema_top_frame_color =tema_data["CTkFrame"]["top_fg_color"]
        tema_progressbar_fondo  = tema_data["CTkProgressBar"]["fg_color"]
        print(tema_frame_color)
        print(tema_botones_color)
    else: 
        ruta_tema = os.path.join(os.path.dirname(ctk.__file__), "assets\\themes", f"{tema_ruta}.json")
        print(ruta_tema)
        # Cargar el JSON
        with open(ruta_tema, "r") as f:
            tema_data = json.load(f)
        tema_botones_color = tema_data["CTkButton"]["fg_color"]
        tema_frame_color =tema_data["CTkFrame"]["fg_color"]
        tema_top_frame_color =tema_data["CTkFrame"]["top_fg_color"]
        print(tema_frame_color)
        print(tema_botones_color)
        

#-------------------FUENTES------------------------
FUENTE_PRINCIPAL = "Comic Sans MS" 
FUENTE_TITULO = (FUENTE_PRINCIPAL, 40, "bold")
FUENTE_SUBTITULOS =(FUENTE_PRINCIPAL, 25)
FUENTE_PEQUEÑA =(FUENTE_PRINCIPAL, 15, "bold")
#-------------------PADINGS------------------------
PADX = 5
PADY = 5
CORNER_RADIUS = 5
#---------------------TEMAS------------------------
FONDOS = ["light",
         "dark",
         "system",]
TEMAS_PERSONALIZADOS = ["autumn",
         "breeze",
         "carrot",
         "cherry",
         "coffee",
         "lavender",
         "marsh",
         "metal",
         "midnight",
         "orange",
         "patina",
         "pink",
         "red",
         "rime",
         "rose",
         "sky",
         "violet",
         ]
TEMAS_COLOR_DEFAULT =["dark-blue","green","blue"]

#COLORES PRINCIPALES 
COLOR_BARRA_PRINCIPAL = "#303030"
COLOR_CONTRASTE = "#0fa987"
COLOR_FRENTE = "#333333"
COLOR_FONDO = "#2b2b2b"
#COLOR_BORDE = "#f08c00"
COLOR_BORDE = "white"
#COLORES = ["#5d5f5e","#ffc9c9","#b2f2bb","#ffec99","#a5d8ff","#1971c2"]
#COLORES = [
#    "#D72638",  # Rojo intenso
#    "#0057E7",  # Azul eléctrico
#    "#00A86B",  # Verde lima
#    "#FF6F00",  # Naranja vibrante
#    "#6A0DAD"   # Morado real
#]
COLORES= [
    "#B23A48",  # Rojo mate
    "#3B6BA5",  # Azul mate
    "#4F8A77",  # Verde mate
    "#CC7722",  # Naranja quemado
    "#7E5A9B"   # Morado suave
]