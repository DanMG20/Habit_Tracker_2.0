from pathlib import Path
import sys
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
        print(DIRECCION_JSON)
        return  DIRECCION_JSON
