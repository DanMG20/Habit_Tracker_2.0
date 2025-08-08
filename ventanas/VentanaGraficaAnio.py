import customtkinter as ctk 
import estilos
from VentanaGraficaMes import VentanaGraficaMes
from fechas import fechas


class VentanaGraficaAnio(VentanaGraficaMes):

    def __init__(self):
        super().__init__()
        self.anio = fechas.encabezados_fechas()[3]
        self.crear_frame_botones_navegacion("Rendimiento semanal")
        self.crear_label_rendimiento("Rendimiento en el año 15%")
        self.crear_frame_control(self.anio)
        self.crear_frame_grafica()

ventana= VentanaGraficaAnio()
ventana.mainloop()
    
