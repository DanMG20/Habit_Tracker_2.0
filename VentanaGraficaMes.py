import customtkinter as ctk 
import estilos
from VentanaPrincipal import VentanaPrincipal
from fechas import fechas

class VentanaGraficaMes(VentanaPrincipal):
    def __init__(self):
        super().__init__()
        mes = fechas.encabezados_fechas()[2]
        self.crear_frame_botones_navegacion("Rendimiento anual")
        self.crear_label_rendimiento("Rendimiento en el mes 12%")
        self.crear_frame_control(mes)
        self.crear_frame_grafica()
    

    def crear_frame_grafica(self): 
        frame_grafica_mensual = ctk.CTkFrame(self)
        frame_grafica_mensual.grid(row = 2, column= 0 , columnspan = 4 ,rowspan = 8,sticky = "nsew",
                                   padx= estilos.PADX, pady =estilos.PADY)
    def crear_frame_botones_navegacion(self,label_bot_rendimiento): 
        self.frame_botones_navegacion = ctk.CTkFrame(self)
        self.frame_botones_navegacion.grid(row= 1, column = 0, sticky ="nsew",padx= estilos.PADX, pady =estilos.PADY)
        #configurar frame 
        self.frame_botones_navegacion.rowconfigure(0, weight=1)
        for column in range (2):
            self.frame_botones_navegacion.columnconfigure (column, weight=1)
        #Boton ventana principal 
        boton_ventana_principal = ctk.CTkButton(self.frame_botones_navegacion,
                                                 text ="Ventana principal", font=estilos.FUENTE_SECUNDARIA)
        boton_ventana_principal.grid(row=0, column = 0, sticky ="nsew")
        #Boton ventana rend
        boton_ventana_rendimiento = ctk.CTkButton(self.frame_botones_navegacion,
                                                text = label_bot_rendimiento, font=estilos.FUENTE_SECUNDARIA)
        boton_ventana_rendimiento.grid(row=0, column = 1, sticky ="nsew")
    def regresar_a_ventana_principal(self): 
        self.destroy()
        pass
        


