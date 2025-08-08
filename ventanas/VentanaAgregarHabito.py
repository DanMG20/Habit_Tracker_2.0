import customtkinter as ctk 
import estilos
from ventanas.ConfigVentana import VentanaComun

class VentanaAgregarHabito (VentanaComun):
    def __init__(self): 
        super().__init__()
        self.nombre_ventana()
        self.crear_frame_izquierdo()
        self.crear_frame_semana()

    def nombre_ventana (self):
        label_nombre_ventana = ctk.CTkLabel(self, text ="AGREGAR HABITO",
                                    font = estilos.FUENTE_SECUNDARIA,
                                    fg_color=estilos.COLOR_ENFRENTE)
        label_nombre_ventana.grid(column =0, row = 1, columnspan = 4, sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY )

    def crear_frame_izquierdo(self):
        self.frame_izquierdo = ctk.CTkFrame(self)
        self.frame_izquierdo.grid(column=0, row= 2 , rowspan = 4,sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY )
        self.nombre_habito()
        self.color_habito()
        self.configurar_frame_izquierdo()
        self.crear_frame_botones_navegacion()
    def configurar_frame_izquierdo(self): 
        self.frame_izquierdo.columnconfigure(0, weight=1)
        for fila in range (4):
            self.frame_izquierdo.rowconfigure(fila, weight=1)
    def configurar_frame_semana(self):
        self.frame_selec_semana.columnconfigure(0, weight=1)
        for fila in range (3):
            self.frame_selec_semana.rowconfigure(fila , weight=1)

    def nombre_habito (self): 
        #label
        label_nombre = ctk.CTkLabel(self.frame_izquierdo, text ="INGRESA EL NOMBRE DE TU NUEVO HABITO",
                                    font = estilos.FUENTE_PEQUEÑA,
                                    fg_color=estilos.COLOR_ENFRENTE)
        label_nombre.grid (column = 0 , row = 0, sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY)
        #Entry 
        Entry_nombre = ctk.CTkEntry(self.frame_izquierdo,
                                    font = estilos.FUENTE_PEQUEÑA,
                                    fg_color=estilos.COLOR_ENFRENTE)
        Entry_nombre.grid (column = 0 , row = 1, sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY)
    def color_habito (self): 
        #label
        label_nombre = ctk.CTkLabel(self.frame_izquierdo, text ="ELIGE EL COLOR DE TU NUEVO HABITO",
                                    font = estilos.FUENTE_PEQUEÑA,
                                    fg_color=estilos.COLOR_ENFRENTE)
        label_nombre.grid (column = 0 , row = 2, sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY)
        #frame
        frame_colores = ctk.CTkFrame(self.frame_izquierdo,)
        frame_colores.grid(column=0 ,row = 3, sticky="nsew",padx= estilos.PADX, pady =estilos.PADY)
        #Crear botones colores 
        for color in estilos.COLORES: 
            boton_color = ctk.CTkButton(frame_colores,
                                        fg_color=color,
                                        width = 60,
                                        height=60,
                                        text="")
            boton_color.pack(side="left",expand= True)
    def crear_frame_semana (self): 
        self.frame_selec_semana = ctk.CTkFrame(self)
        self.frame_selec_semana.grid(column=1, row= 2 ,columnspan =3, rowspan = 3,sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY )
        self.dias_repeticion()
        self.configurar_frame_semana()

    def dias_repeticion(self):
        #label
        label_semana = ctk.CTkLabel(self.frame_selec_semana, text ="DIAS DE LA SEMANA",
                                    font = estilos.FUENTE_PEQUEÑA,
                                    fg_color=estilos.COLOR_ENFRENTE)
        label_semana.grid(column = 0 , row = 0,sticky = "nsew",padx= estilos.PADX, pady =estilos.PADY)
        # Seleccionar todos 
        boton_seleccionar_todos = ctk.CTkCheckBox(self.frame_selec_semana, text ="SELECCIONAR TODOS",
                                                  font=estilos.FUENTE_PEQUEÑA)
        boton_seleccionar_todos.grid(column = 0,row = 2,sticky = "e",padx= 40, pady =estilos.PADY)
        #frame botones
        self.frame_dias_semana = ctk.CTkFrame(self.frame_selec_semana)
        self.frame_dias_semana.grid(column=0 ,row = 1, sticky="nsew",padx= estilos.PADX, pady =estilos.PADY)
        self.crear_botones_semana()

    def crear_botones_semana(self):
        semana = ("D","L","M","M","J","V","S") 
        for dia in semana: 
            boton_color = ctk.CTkButton(self.frame_dias_semana,
                                        fg_color=estilos.COLOR_BOTONES_SEMANA,
                                        font=estilos.FUENTE_PEQUEÑA,
                                        width = 60,
                                        height=60,
                                        text=dia)
            boton_color.pack(side="left",padx = 13,expand =True)
    def crear_frame_botones_navegacion(self): 
        frame_botones_navegacion = ctk.CTkFrame(self)
        frame_botones_navegacion.grid(column=1,row=5, columnspan=3,sticky="nsew",padx= estilos.PADX, pady =estilos.PADY)
        frame_botones_navegacion.rowconfigure(0,weight=1)
        for columna in range(2):
            frame_botones_navegacion.columnconfigure(columna, weight=1)
        boton_cancelar = ctk.CTkButton(frame_botones_navegacion,
                                       text="CANCELAR",
                                       fg_color=estilos.COLOR_BOTONES_SEMANA,
                                       font=estilos.FUENTE_SECUNDARIA)
        boton_cancelar.grid(column=0, row = 0,sticky="nsew",padx= estilos.PADX, pady =estilos.PADY )
        boton_agregar_habito =ctk.CTkButton(frame_botones_navegacion,
                                            text ="AGREGAR HABITO",
                                            fg_color=estilos.COLOR_BOTONES_SEMANA,
                                            font=estilos.FUENTE_SECUNDARIA,)
        boton_agregar_habito.grid(column=1, row = 0,sticky="nsew",padx= estilos.PADX, pady =estilos.PADY )
    
