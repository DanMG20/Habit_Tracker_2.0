from pathlib import Path
import sys
import os
# Direcciones 
def obtener_direccion_icono():
    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    DIRECCION_ICONO = base_path / "sources" / "icono_principal.ico"
    return str(DIRECCION_ICONO)  # <--- Convertir a string



def obtener_direccion_icono_top():
    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent
    DIRECCION_ICONO = base_path / "sources" / "icono_principal_copy.ico"
    return str(DIRECCION_ICONO)  # <--- Convertir a string

def obtener_direccion_dir_json():
        if getattr(sys, 'frozen', False):
            # PyInstaller ejecutándose
            base_path = Path(sys._MEIPASS)
        else:
            # En desarrollo
            base_path = Path(__file__).parent
        DIRECCION_JSON = base_path / "json"
        return  DIRECCION_JSON

def direccion_config(relative_path):
    """Obtiene la ruta absoluta al recurso, funciona para PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # Ejecutando desde .exe
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def resource_path(relative_path):
    """ Obtiene la ruta absoluta del recurso, funciona para dev y para .exe """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

