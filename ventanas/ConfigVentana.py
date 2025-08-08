import customtkinter as ctk 
import json
from pathlib import Path
import os
import estilos


direccion_archivo_posicion_ventana  = Path("json\\posicion_ventana.json")

def guardar_posicion_ventana(ventana):
    x = ventana.winfo_x()
    y = ventana.winfo_y()
    datos = {
        "posicion": {"x": x, "y": y},
    }


    with direccion_archivo_posicion_ventana.open("w") as f:
         json.dump(datos, f)
def cargar_posicion_ventana(ventana):
        # Verificar si el archivo existe
        if os.path.exists(direccion_archivo_posicion_ventana):
            with open(direccion_archivo_posicion_ventana, "r") as f:
                datos = json.load(f)
                posicion = datos["posicion"]
                ventana.geometry(f"+{posicion['x']}+{posicion['y']}")
        else:
            # Si no existe el archivo, centrar la ventana
            ventana.update_idletasks()  # Asegura que se obtengan los valores correctos de tamaño
            screen_width = ventana.winfo_screenwidth()
            screen_height = ventana.winfo_screenheight()
            ventana.geometry(
                f"800x600+{(screen_width - 800) // 2}+{(screen_height - 600) // 2}")  # Ajusta el tamaño predeterminado si es necesario




