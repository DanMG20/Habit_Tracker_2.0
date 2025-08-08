import customtkinter as ctk 
from PIL import Image, ImageTk
import estilos
from direcciones import obtener_direccion_icono
from ventanas.ConfigVentana import *
from Fechas import Fechas
from datetime import *
from Database import Database


class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        #----------------------------------------------------------MAIN CONFIG -------------------------------------------------------
        self.title("Habit Tracker- by Elchilakas")
        self.iconbitmap(obtener_direccion_icono())
        #Ajustar pantalla
        #cargar_posicion_ventana(self)
        cargar_posicion_ventana(self)
        #------------------------------------------OBJETOS----------------------------------------------------------------------------
        self.db_objeto = Database()
        self.fechas_objeto = Fechas(db_objeto =self.db_objeto)
        #-----------------------------------------VARIABLES---------------------------------------------------------------------------
    
        #-------------------------------------------INICIALIZAR APP-------------------------------------------------------------------
        self.inicializar_frames_constantes()
        self.inicializar_todos_los_frames()
      
        #self.inicializar_frames_ventana_principal()
        #------------------------------------------CONFIG BOTONES -------------------------------------------------------------------
        #self.config_botones_semana()
        #self.actualizar_programa()
        #------------------------------------------PARA QUE LA VENTANA SE HABRA EN ZOOM-----------------------------------------------
        self.after_idle(lambda: self.state("zoomed"))
                #Guardar posicion de la pantalla al cerrarse 
        self.protocol("WM_DELETE_WINDOW",
             lambda: (guardar_posicion_ventana(self), self.destroy()))
        
        
#---------------------------------------------FUNCIONES DE INICIALIZACION------------------------------------------------------------


    def inicializar_frames_constantes(self):
        self.mostrar_frames_top()
        self.configuracion_grillado()

    def inicializar_todos_los_frames(self):
        self.frames_ventana_principal()

    def frames_ventana_principal(self):
        self.mostrar_frame_fecha_hoy_1_0()
        self.mostrar_frame_rendimiento_1_1()
        self.mostrar_frame_control_1_2()
        self.mostrar_frame_btn_completar_2_0()
        frames_ventana_principal = [self.frame_fecha_hoy_1_0]




    def inicializar_frames_izq(self):
        self.contenedor_izq= ctk.CTkFrame(self,fg_color ="white")
        self.contenedor_izq.grid(
            row =1,
            column=0,
            rowspan=7,
            sticky ="nsew",
            padx= estilos.PADX,
            pady =estilos.PADY
            )
        self.contenedor_izq.rowconfigure(0, weight=1)
        self.contenedor_izq.columnconfigure(0, weight=1)
        self.frames_izq = {}

        for FrameClase in [AgregarHabitoFrameIzq,FramePrincipalIzq]:
            frame = FrameClase(self.contenedor_izq, self)
            self.frames_izq[FrameClase.__name__] = frame
            frame.grid(row=0, column = 0 , sticky = "nsew")
    
    def inicializar_frames_der(self):
        self.contenedor_der= ctk.CTkFrame(self,fg_color ="white")
        self.contenedor_der.grid(
            row =1,
            column=1,
            columnspan=3,
            rowspan=7,
            sticky ="nsew",
            padx= estilos.PADX,
            pady =estilos.PADY
            )
        self.contenedor_der.rowconfigure(0, weight=1)
        self.contenedor_der.columnconfigure(0, weight=1)
        self.frames_der = {}

        for FrameClase in [AgregarHabitoFrameDer,FramePrincipalDer]:
            frame = FrameClase(self.contenedor_der, self)
            self.frames_der[FrameClase.__name__] = frame
            frame.grid(row=0, column = 0 , sticky = "nsew")
#---------------------------------------------FRAMES CONSTANTES-----------------------------------------------------------
    def mostrar_frames_top(self):
         #------------------------------------FRAMES TITULO---------------------------------------------------------------
        self.frame_titulo_icono_0_0 = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_titulo_icono_0_0.grid(
            row = 0,column =0,
            sticky = "ew",
            padx=estilos.PADX,
            pady=estilos.PADY,
            )
        #-----------------------------------------ICONO---------------------------------------------------------------
        img_icono = ctk.CTkImage(light_image=Image.open(obtener_direccion_icono()),
                      dark_image=Image.open(obtener_direccion_icono()),
                      size=(100, 100))
        
        icono_label = ctk.CTkLabel(self.frame_titulo_icono_0_0, image=img_icono, text="")
        icono_label.pack(
            side="left",
            fill="x",
            padx=5,
            pady=10)
        #-----------------------------------------TITULO---------------------------------------------------------------
        tituloapp_label = ctk.CTkLabel(self.frame_titulo_icono_0_0, font=estilos.FUENTE_TITULO, text ="HABIT TRACKER")
        tituloapp_label.pack(
            side="right",
            fill="x",
            padx = (0,15),
            pady=10)
        #-------------------------------------FRAME FRASE ------------------------------------------------------------------
        self.frame_frase_0_1=ctk.CTkFrame(self, corner_radius=estilos.CORNER_RADIUS)
        self.frame_frase_0_1.grid(
            row=0,
            column = 1,
            columnspan = 3,
            sticky ="nsew",
            padx = estilos.PADX,
            pady = estilos.PADY,
            )
        frase_label = ctk.CTkLabel(
            self.frame_frase_0_1,
            text= "Frase del día:\nSomos lo que hacemos - Sócrates",
            anchor="center",
            font=estilos.FUENTE_SUBTITULOS,
            )
        frase_label.pack(
            fill="both",
            padx= estilos.PADX,
            pady= estilos.PADY
            )
        
    def configuracion_grillado(self): 
        for columna in range(1,2):
            self.columnconfigure(columna, weight=1)
        for fila in range(2,4):
            self.rowconfigure(fila, weight=1)

    
    def mostrar_frame_fecha_hoy_1_0(self): 
        self.frame_fecha_hoy_1_0 = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_fecha_hoy_1_0.grid(
            row = 1,
            column = 0,
            sticky = "nsew",
            pady = estilos.PADY,
            padx= estilos.PADX
            )
              # configurar expansion del frame 
        self.fecha_hoy_label = ctk.CTkLabel(
            self.frame_fecha_hoy_1_0,
            text ="Hoy Miércoles 29",
            anchor ="center",
            font = estilos.FUENTE_SUBTITULOS)
        self.fecha_hoy_label.pack(
            fill ="both",
            pady= estilos.PADY,
            padx= estilos.PADX)

    def mostrar_frame_rendimiento_1_1(self): 
        self.frame_rendimiento = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_rendimiento.grid(
            row =1,
            column= 1,
            sticky="nsew",
            padx=estilos.PADX,
            pady =estilos.PADY
            )
        self.barra_rendimiento = ctk.CTkProgressBar(
            self.frame_rendimiento,
            progress_color=estilos.COLOR_CONTRASTE,
            corner_radius=estilos.CORNER_RADIUS*2)
        self.barra_rendimiento.pack(
            side="left",
            fill="both",
            expand=True,
            padx=estilos.PADX,
            pady=estilos.PADY
            )
        self.label_rendimiento= ctk.CTkLabel(
            self.frame_rendimiento,
            text ="5%",
            font = estilos.FUENTE_SUBTITULOS)
        self.label_rendimiento.pack(
            side="right",
            fill="both",
            padx= estilos.PADX*2,
            pady= estilos.PADY
            )

    def mostrar_frame_control_1_2(self): 
        frame_controles = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        frame_controles.grid(
            row = 1,
            column = 2,
            sticky="nsew",
            padx= estilos.PADX,
            pady = estilos.PADY
        )
        self.boton_izq = ctk.CTkButton(
            frame_controles,
            text ="<",
            font = estilos.FUENTE_SUBTITULOS,
            fg_color=estilos.COLOR_CONTRASTE,
            corner_radius=estilos.CORNER_RADIUS)
        self.boton_izq.pack(
            side ="left",
            fill="both",
            padx=estilos.PADX,
            pady=estilos.PADY
            )
        self.label_f_control = ctk.CTkLabel(
            frame_controles,
            text = "Semana 32",
            font =estilos.FUENTE_SUBTITULOS,
            anchor ="center",
            corner_radius=estilos.CORNER_RADIUS)
        self.label_f_control.pack(
            side ="left",
            fill="both",
            padx=estilos.PADX,
            pady=estilos.PADY
            )
        self.boton_der = ctk.CTkButton(
            frame_controles,
            text= ">",
            font=estilos.FUENTE_SUBTITULOS,
            fg_color=estilos.COLOR_CONTRASTE,
            corner_radius=estilos.CORNER_RADIUS)
        self.boton_der.pack(
            side ="left",
            fill="both",
            padx=estilos.PADX,
            pady=estilos.PADY
            )

    def mostrar_frame_btn_completar_2_0(self):
        self.frame_btn_completar = ctk.CTkScrollableFrame(
            self,
            corner_radius=estilos.CORNER_RADIUS
        )
        self.frame_btn_completar.grid(
            row=2,
            column=0,
            rowspan = 2, 
            padx= estilos.PADX,
            pady= estilos.PADY
        )
        self.frame

    
#---------------------------------------------FUNCIONES DE ACTUALIZACION-----------------------------------------------------------
    def actualizar_programa(self):
        print("El programa se ha actualizado")
        self.refrescar_tabla_y_fechas(None)
        self.crear_linea_fecha()
        # Reprogramar la ejecución después de 900,000 ms (15 min)
        self.after(900000, self.actualizar_programa)
    
    def refrescar_ventana_principal(self, event):
        self.crear_botones_habitos_completar()
        self.crear_frame_tabla_habitos()
        self.rendimiento_semanal = self.fechas_objeto.calcular_rendimiento_semanal()/100
        self.label_porcentaje.configure(text =f"{round(self.rendimiento_semanal*100)} %") 
        self.barra_rendimiento.set(self.rendimiento_semanal)
        self.state("zoomed")
  
    def refrescar_tabla_y_fechas(self,event):
                # Actualizar fechas antes de redibujar
        self.fechas_objeto.actualizar_valores()
        rendimiento =self.fechas_objeto.calcular_rendimiento_semanal()
        self.barra_rendimiento.set(rendimiento/100)
        self.label_porcentaje.configure(text =f"{round(rendimiento)} %")
        # Actualizar label del control de semana
        self.label_control_actual.configure(text=self.semana)
        # Redibujar los encabezados y tabla de hábitos
        self.crear_frame_contenedor_habitos()

#-------------------------------------------------------EVENTOS--------------------------------------------------------------------
    def evento_semana_anterior(self):
        self.fechas_objeto.mostrar_semana_anterior()
        self.semana = self.fechas_objeto.encabezados_fechas()[1]
        self.dias_actuales = self.fechas_objeto.dias_actuales()
        self.inicio_semana = self.fechas_objeto.inicio_semana()[0]
        self.inicio_semana_fecha = self.fechas_objeto.inicio_semana()[1]
        self.label_control_actual.configure(text = self.semana)

        self.refrescar_tabla_y_fechas(None)
        
    def evento_semana_siguiente(self):
        self.fechas_objeto.mostrar_semana_siguiente()
        self.semana = self.fechas_objeto.encabezados_fechas()[1]
        self.dias_actuales = self.fechas_objeto.dias_actuales()
        self.inicio_semana = self.fechas_objeto.inicio_semana()[0]
        self.inicio_semana_fecha = self.fechas_objeto.inicio_semana()[1]
        self.label_control_actual.configure(text = self.semana)
        self.refrescar_tabla_y_fechas(None)

    def evento_marcar_habito(self,nombre_habito): 
        self.db_objeto.registrar_ejecucion_habito(nombre_habito)
        self.refrescar_ventana_principal(None)



#------------------------------Configura los botones para navegar entre semanas---------------------------------------------------
    def mostrar_frame(self, nombre_frame):
        frame = self.frames_izq[nombre_frame]
        self.frame_contenedor.tkraise()
        frame.tkraise()
    
   
    def mostrar_frames_agregar_habito(self):
        frame_izq = self.frames_izq["AgregarHabitoFrameIzq"]
        #self.frames_izq.tkraise()
        frame_der = self.frames_der["AgregarHabitoFrameDer"]
        #self.frames_der.tkraise()
        frame_der.tkraise()
        frame_izq.tkraise()


