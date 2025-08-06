from pathlib import Path
import sys
# Direcciones 
def obtener_direccion_icono():
    if getattr(sys, 'frozen', False):
        # PyInstaller ejecutándose
        base_path = Path(sys._MEIPASS)
    else:
        # En desarrollo
        base_path = Path(__file__).parent
    DIRECCION_ICONO = base_path / "sources" / "icono_principal.ico"
    return  DIRECCION_ICONO
