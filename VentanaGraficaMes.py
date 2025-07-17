import customtkinter as ctk 
import estilos
from VentanaComun import VentanaComun

class VentanaGraficaMes(VentanaComun):
    def __init__(self):
        super().__init__()
        self.crear_frame_botones()
        self.configurar_frame_botones()
        self.crear_frame_grafica()
    def crear_frame_botones(self):
        #crear frame 
        self.frame_botones= ctk.CTkFrame(self)
        self.frame_botones.grid(row =1, column = 0 ,columnspan = 4, sticky="nsew",padx= estilos.PADX, pady =estilos.PADY)
        # Crear botones 
        self.boton_regresar_ventana_principal = ctk.CTkButton(self.frame_botones, text = "Regresar a ventana principal",
                                                               font=estilos.FUENTE_SECUNDARIA)
        self.boton_regresar_ventana_principal.grid(column=0,row=0 , sticky="nsew")

        self.boton_ventana_rend_anual = ctk.CTkButton(self.frame_botones, text = "Rendimiento anual",
                                                               font=estilos.FUENTE_SECUNDARIA)
        self.boton_ventana_rend_anual.grid(column=1 , row=0 , sticky  ="nsew")
        self.label_rendimiento_mens = ctk.CTkLabel(self.frame_botones, text = "Rendimiento este mes 29%", font=estilos.FUENTE_SECUNDARIA)
        self.label_rendimiento_mens.grid(column=2,row=0 , sticky="nsew")
        #FRAME CONTROLES MES 
        self.frame_control_mes= ctk.CTkFrame(self.frame_botones)
        self.frame_control_mes.grid(row= 0, column = 3 , columnspan = 2, sticky = "nsew")

        boton_izq = ctk.CTkButton(self.frame_control_mes,text= "<")
        boton_izq.pack(side="left")
        boton_der= ctk.CTkButton(self.frame_control_mes, text = ">")
        boton_der.pack(side="right")
        label_mes_actual = ctk.CTkLabel(self.frame_control_mes,
                                                text= "Enero",justify= "center",  font =estilos.FUENTE_SECUNDARIA)
        label_mes_actual.pack(anchor = "center", expand = True )
    def configurar_frame_botones( self):
        self.frame_botones.rowconfigure(0, weight=1)
        for columna in range(4): 
            self.frame_botones.columnconfigure(columna,weight=1)

    def crear_frame_grafica(self): 
        frame_grafica_mensual = ctk.CTkFrame(self)
        frame_grafica_mensual.grid(row = 2, column= 0 , columnspan = 4 ,rowspan = 8,sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY)




ventana_grafica_mes = VentanaGraficaMes()
ventana_grafica_mes.mainloop()