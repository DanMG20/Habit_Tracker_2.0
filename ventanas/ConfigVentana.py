
import json
from pathlib import Path
from direcciones import resource_path  # Asegúrate de tener esta función

# Rutas de archivos usando Path
direccion_archivo_posicion_ventana = Path("json/posicion_ventana.json")
config_path = Path("json/configuracion.json")

def guardar_posicion_ventana(ventana):
    archivo_real = Path(resource_path(direccion_archivo_posicion_ventana))
    archivo_real.parent.mkdir(parents=True, exist_ok=True)

    x = ventana.winfo_x()
    y = ventana.winfo_y()
    datos = {"posicion": {"x": x, "y": y}}

    with archivo_real.open("w") as f:
        json.dump(datos, f)


def cargar_posicion_ventana(ventana):
    archivo_real = Path(resource_path(direccion_archivo_posicion_ventana))

    if archivo_real.exists():
        with archivo_real.open("r") as f:
            datos = json.load(f)
            posicion = datos.get("posicion", {"x": 100, "y": 100})
            ventana.geometry(f"+{posicion['x']}+{posicion['y']}")
    else:
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        ventana.geometry(
            f"800x600+{(screen_width - 800) // 2}+{(screen_height - 600) // 2}"
        )
