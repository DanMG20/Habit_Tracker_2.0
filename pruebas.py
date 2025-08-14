import json 
import os
import customtkinter as ctk
from pathlib import Path
configuracion = Path("json\\configuracion.json")

with open(configuracion, "r") as f: 
    data = json.load(f)
    tema_ruta = data["TEMA_SELECCIONADO"]
    if "\\" in tema_ruta: 
        ruta = tema_ruta
        with open (ruta, "r") as file:
            tema_data = json.load(file)

        print(tema_data["CTkFrame"]["fg_color"])
        print(tema_data["CTkButton"]["fg_color"])
    else: 
        ruta_tema = os.path.join(os.path.dirname(ctk.__file__), "assets\\themes", f"{tema_ruta}.json")
        print(ruta_tema)
        # Cargar el JSON
        with open(ruta_tema, "r") as f:
            tema_data = json.load(f)

        print(tema_data["CTkFrame"]["fg_color"])
        print(tema_data["CTkButton"]["fg_color"])