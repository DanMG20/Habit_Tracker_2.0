import customtkinter as ctk 
from PIL import Image
import estilos
import sys
from direcciones import obtener_direccion_icono,resource_path
#from CTkMenuBar import *
from CTkMenuBarPlus import *
from ventanas.VentanaFuente import *
from ventanas.VentanaAgregarHabito import *
from ventanas.VentanaGraficaMes import * 
from ventanas.ConfigVentana import *
from ventanas.VentanaEliminarHabito import * 
from ventanas.VentanaAgregarFrase import * 
from ventanas.VentanaAcercaDe import *
from ventanas.VentanaGraficaAnio import *
from Fechas import Fechas
from datetime import *
from Database import Database


class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
       
        #----------------------------------------------------------MAIN CONFIG -------------------------------------------------------
        self.title("")
        self.iconbitmap(obtener_direccion_icono())
        #------------------------------------------OBJETOS----------------------------------------------------------------------------
        self.db_objeto = Database(master=self)
        self.fechas_objeto = Fechas(db_objeto =self.db_objeto)
        
        

        self.db_objeto.cargar_frases_random()
        self.cargar_configuracion()
        #-----------------------------------------VARIABLES---------------------------------------------------------------------------
        self.DIA_HOY = self.fechas_objeto.DIA_HOY
        self.dia_AYER =self.fechas_objeto.DIA_AYER
        self.inicializar_variables_fechas()
        self.width_column_habitos_tabla = 350 
        self.estado_boton_eliminar_habito = False
        self.estado_boton_marcar_ayer = False
        #Ajustar pantalla
        
        cargar_posicion_ventana(self)
        #-------------------------------------------INICIALIZAR APP-------------------------------------------------------------------
        self.inicializar_frames_constantes()
        self.inicializar_todos_los_frames()
        self.configuracion_grillado()
        self.grafica_anio_objeto = VentanaGraficaAnio(
                self,
                self.frames_ventana_principal_lista,
                self.db_objeto,self.fechas_objeto,
            )
        self.obj_ventana_grafica_mes = VentanaGraficaMes(
            self,
            self.frames_ventana_principal_lista,
            self.db_objeto,self.fechas_objeto,
            self.grafica_anio_objeto)
        #------------------------------------------CONFIG BOTONES -------------------------------------------------------------------
        self.configurar_controles_semanales()
        #self.actualizar_programa()
        self.ventana_agregar_habito.evento_btn_cancelar()
        #------------------------------------------PARA QUE LA VENTANA SE HABRA EN ZOOM-----------------------------------------------
        self.after_idle(lambda: self.state("zoomed"))
                #Guardar posicion de la pantalla al cerrarse 
        self.protocol("WM_DELETE_WINDOW", self.al_cerrar)
        
    def al_cerrar(self):
        guardar_posicion_ventana(self)  # guarda la posición
        self.unbind("<Configure>")
        self.destroy()                   # cierra la ventana
        
#---------------------------------------------FUNCIONES DE INICIALIZACION------------------------------------------------------------
    def inicializar_variables_fechas(self):
        self.encabezados= self.fechas_objeto.encabezados_fechas()
        self.inicio_semana = self.fechas_objeto.inicio_semana()
        self.dias_actuales = self.fechas_objeto.dias_actuales()
        self.rendimiento_semanal = self.fechas_objeto.calcular_rendimiento_semanal()

    def inicializar_frames_constantes(self):
        self.mostrar_frames_top()
        self.barra_menu()

    def frames_ventana_agregar_habito(self):
        self.ventana_agregar_habito = VentanaAgregarHabito(self,self.frames_ventana_principal_lista,self.db_objeto,self.fechas_objeto)

    def frames_ventana_eliminar_habito(self):
        self.obj_eliminar_habito = VentanaEliminarHabito(self,self.db_objeto,self.fechas_objeto)

    def frames_ventana_grafica(self):
        if hasattr(self, "obj_ventana_grafica_mes") and self.obj_ventana_grafica_mes:
            self.obj_ventana_grafica_mes.inicializar_frames_graf_mensual()

         #   self.obj_ventana_grafica_mes.frame_grafica_mensual.grid(
         #   row=3,
        #    column=0,
        #    columnspan =3,
        #    sticky="nsew",
        #    rowspan = 3, 
        #    padx= estilos.PADX,
        #    pady= estilos.PADY
       # )
            
    def frames_ventana_grafica_anio(self):
        if hasattr(self, "grafica_anio_objeto") and self.grafica_anio_objeto:
            # Solo actualizar la gráfica existente
        
        
    
            self.grafica_anio_objeto.abrir_frames()
            self.grafica_anio_objeto.frame_grafica_anual.grid(
            row=3,
            column=0,
            columnspan =3,
            sticky="nsew",
            rowspan = 3, 
            padx= estilos.PADX,
            pady= estilos.PADY
            )
        else:
        
            self.grafica_anio_objeto = VentanaGraficaAnio(
                self,
                self.frames_ventana_principal_lista,
                self.db_objeto,self.fechas_objeto,
            )
     


    def inicializar_todos_los_frames(self):
        self.frames_ventana_principal()
        self.frames_ventana_agregar_habito()
        self.frames_ventana_eliminar_habito()
        self.mostrar_frame_marcar_ayer()
        
    def frames_ventana_principal(self):
        self.mostrar_frame_fecha_hoy_1_0()
        self.mostrar_frame_rendimiento_1_1()
        self.mostrar_frame_control_1_2()
        self.mostrar_frame_btn_completar_2_0()
        self.mostrar_frame_tabla_habitos_3_1()
        self.mostrar_frame_nav_4_1()
        self.frames_ventana_principal_lista = [self.frame_fecha_hoy_1_0,
                                    self.frame_rendimiento,
                                    self.frame_controles,
                                    self.frame_btn_completar_contenedor,
                                    self.frame_tabla_habitos_contenedor,
                                    self.frame_nav,
                                    self.frame_encabezado
                                    ]
    
#---------------------------------------------FRAMES CONSTANTES-----------------------------------------------------------
    def mostrar_frames_top(self):
         #------------------------------------FRAMES TITULO---------------------------------------------------------------
        self.frame_titulo_icono_0_0 = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_titulo_icono_0_0.grid(
            row = 1,column =0,
            sticky = "ew",
            padx=estilos.PADX,
            pady=(estilos.PADY*2,estilos.PADY),
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
            padx = (0,30),
            pady=10)
        #-------------------------------------FRAME FRASE ------------------------------------------------------------------
        self.frame_frase_0_1=ctk.CTkFrame(self, corner_radius=estilos.CORNER_RADIUS)
        self.frame_frase_0_1.grid(
            row=1,
            column = 1,
            columnspan = 3,
            sticky ="nsew",
            padx = estilos.PADX,
            pady=(estilos.PADY*2,estilos.PADY),
            )


        self.frame_frase_0_1.grid_rowconfigure(0, weight=1)
        self.frame_frase_0_1.grid_columnconfigure(0, weight=1)
        self.mostrar_frase()
        # ---------- encabezado ----------

        # ---------- frase ----------
    def mostrar_frase(self):
        self.label_frase = ctk.CTkLabel(
            self.frame_frase_0_1,
            text=f"“{self.db_objeto.frase_seleccionada}”",
            justify="center",
            wraplength=620,              # ajusta el ancho del texto
            font=estilos.FUENTE_FRASE
        )
        self.label_frase.grid(row=0, column=0, padx=28, pady=(16, 2), sticky="n")

        # ---------- autor ----------
        self.label_autor = ctk.CTkLabel(
            self.frame_frase_0_1,
            text=f"— {self.db_objeto.autor_frase}",
            font=estilos.FUENTE_AUTOR,
            text_color=estilos.COLOR_AUTOR
        )
        self.label_autor.grid(row=1, column=0, padx=18, pady=(0, 16), sticky="n")

    def configuracion_grillado(self): 
        #----------------------------------------------PRINCIPAL
        for columna in range(1,2):
            self.columnconfigure(columna, weight=1)
        self.rowconfigure(4, weight=1)

    def barra_menu(self):
        menu = CTkTitleMenu(master=self)
        button_1 = menu.add_cascade("Tema")
        button_4 = menu.add_cascade("Fuente",
                                    command =self.evento_ventana_fuente
                                    )
        button_2 = menu.add_cascade("Restaurar",
                                    command =self.db_objeto.resetear_archivos
                                    )
        button_3 = menu.add_cascade("Frases")
        self.cascada_boton_3 = CustomDropdownMenu(widget=button_3)
        self.cascada_boton_3.add_option("Agregar Frase", command=self.evento_agregar_frase)
        self.submenu_eliminar_frase =self.cascada_boton_3.add_submenu("Eliminar Frase")
        self.generar_menu_frases()

        button_f = menu.add_cascade("Acerca de",
                                    command= self.evento_acerca_de_ventana)
        dropdown = CustomDropdownMenu(widget=button_1)
        
        #-------------------------------------CAMBIAR- TEMA -------------------------------
        submenu_1 = dropdown.add_submenu("Apariencia") 
        submenu_2 = dropdown.add_submenu("Tema")
        for tema in estilos.FONDOS:
            submenu_1.add_option(option=tema, command= lambda t=tema: self.guardar_configuracion_fondo(t))
        for color in estilos.TEMAS_COLOR_DEFAULT: 
            submenu_2.add_option(option=color,command= lambda c=color: self.evento_cambiar_tema(c))
        for tema_per in estilos.TEMAS_PERSONALIZADOS: 
            submenu_2.add_option(option = tema_per,command= lambda t_p=tema_per: self.evento_cambiar_tema(t_p))

#--------------------------------------------------FRAMES PRINCIPALES-----------------------------------------------------------------
    
    def mostrar_frame_fecha_hoy_1_0(self): 
        self.frame_fecha_hoy_1_0 = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_fecha_hoy_1_0.grid(
            row = 2,
            column = 0,
            sticky = "nsew",
            pady = estilos.PADY,
            padx= estilos.PADX
            )
              # configurar expansion del frame 
        self.fecha_hoy_label = ctk.CTkLabel(
            self.frame_fecha_hoy_1_0,
            text =self.encabezados[0],
            anchor ="center",
            font = estilos.FUENTE_SUBTITULOS)
        self.fecha_hoy_label.pack(
            fill ="both",
            expand=True,
            pady= estilos.PADY,
            padx= estilos.PADX)

    def mostrar_frame_rendimiento_1_1(self): 
        self.frame_rendimiento = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_rendimiento.grid(
            row =2,
            column= 1,
            sticky="nsew",
            padx=estilos.PADX,
            pady =estilos.PADY
            )
        self.barra_rendimiento = ctk.CTkProgressBar(
            self.frame_rendimiento,
            #progress_color=estilos.COLOR_CONTRASTE,
            corner_radius=estilos.CORNER_RADIUS*2)
        self.barra_rendimiento.pack(
            side="left",
            fill="both",
            expand=True,
            padx=estilos.PADX*1.5,
            pady=estilos.PADY*1.5
            )
        self.barra_rendimiento.set(self.rendimiento_semanal/100)
        self.label_rendimiento= ctk.CTkLabel(
            self.frame_rendimiento,
            text =f"{self.rendimiento_semanal}%",
            font = estilos.FUENTE_PEQUEÑA)
        self.label_rendimiento.pack(
            side="right",
            fill="both",
            padx= estilos.PADX*2,
            pady= estilos.PADY
            )
        
    def mostrar_frame_control_1_2(self): 
        self.frame_controles = ctk.CTkFrame(
            self,
            corner_radius=estilos.CORNER_RADIUS,
             width = 100)
        self.frame_controles.grid(
            row = 2,
            column = 2,
            sticky="nsew",
            padx= estilos.PADX,
            pady = estilos.PADY
        )
        self.boton_izq_control = ctk.CTkButton(
            self.frame_controles,
            text ="<",
            font = estilos.FUENTE_SUBTITULOS,
            #fg_color=estilos.COLOR_CONTRASTE,
            corner_radius=estilos.CORNER_RADIUS)
        self.boton_izq_control.pack(
            side ="left",
            fill="both",
            padx=estilos.PADX,
            pady=estilos.PADY
            )
        self.label_f_control = ctk.CTkLabel(
            self.frame_controles,
            text = self.encabezados[1],
            #width= 50,
            font =estilos.FUENTE_SUBTITULOS,
            anchor ="center",
            corner_radius=estilos.CORNER_RADIUS)
        self.label_f_control.pack(
            side ="left",
            fill="both",
            padx=estilos.PADX,
            pady=estilos.PADY
            )
        self.boton_der_control = ctk.CTkButton(
            self.frame_controles,
            text= ">",
            font=estilos.FUENTE_SUBTITULOS,
            #fg_color=estilos.COLOR_CONTRASTE,
            corner_radius=estilos.CORNER_RADIUS)
        self.boton_der_control.pack(
            side ="left",
            fill="both",
            padx=estilos.PADX,
            pady=estilos.PADY
            )

    def mostrar_frame_btn_completar_2_0(self):
        self.frame_btn_completar_contenedor =ctk.CTkFrame(
            self, 
            corner_radius=estilos.CORNER_RADIUS,
        )
        self.frame_btn_completar_contenedor.grid(
            row=3,
            column=0,
            sticky="nsew",
            rowspan = 3, 
            padx= estilos.PADX,
            pady= estilos.PADY
        )
        
        self.frame_btn_completar = ctk.CTkScrollableFrame(
            self.frame_btn_completar_contenedor,
            corner_radius=estilos.CORNER_RADIUS,
            fg_color=estilos.tema_frame_color,
        )
        self.frame_btn_completar.pack(
            fill="both",
            expand = True,
            padx = estilos.PADX,
            pady = estilos.PADY)
        self.listar_habitos()
    
    def mostrar_frame_tabla_habitos_3_1(self):
        self.frame_tabla_habitos_contenedor = ctk.CTkFrame(
            self,
            corner_radius=estilos.CORNER_RADIUS,
            fg_color=estilos.tema_frame_color
            )
        self.frame_tabla_habitos_contenedor.grid(row=3,
                                 column=1,
                                 rowspan=2,
                                 columnspan=2,
                                 sticky="nsew",
                                 pady= estilos.PADY,
                                 padx = estilos.PADX
                                 )
            
        self.frame_tabla_habitos  = ctk.CTkScrollableFrame(
            self.frame_tabla_habitos_contenedor, 
            corner_radius=estilos.CORNER_RADIUS,
            fg_color=estilos.tema_frame_color)
        self.frame_tabla_habitos.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=estilos.PADX,
            pady= estilos.PADY
            )
        self.config_frame_semana()
        self.lista_habitos_frame_semana()
          #----------------------------------------------FRAME TABLA HABITOS
        self.frame_tabla_habitos_contenedor.columnconfigure(0, weight=1)
    
        self.frame_tabla_habitos_contenedor.rowconfigure(1 ,  weight=1)
        self.mostrar_frame_encabezado_tabla_2_1()

    def mostrar_frame_nav_4_1(self): 
        #--------------------------------------------FRAME-------------------
        self.frame_nav = ctk.CTkFrame(self, corner_radius=estilos.CORNER_RADIUS)
        self.frame_nav.grid(
            row=5,
            column=1,
            columnspan =2,
            sticky="nsew",
            padx=estilos.PADX,
            pady=estilos.PADY
        )
        #-------------------------------------------BOTONES-------------------
        self.boton_agregar_hab =ctk.CTkButton(self.frame_nav,
                                              #fg_color=estilos.COLOR_CONTRASTE,
                                              text= "+ Agregar hábito",
                                              command= self.evento_btn_agregar_habito,
                                              font= estilos.FUENTE_SUBTITULOS,
                                              )
        self.boton_agregar_hab.pack(
            side="left",
            fill="x",
            expand=True,
            padx= estilos.PADX,
            pady = estilos.PADY,
        )
        self.boton_eliminar_hab =ctk.CTkButton(self.frame_nav,
                                              #fg_color=estilos.COLOR_CONTRASTE,
                                              text= "- Eliminar hábito",
                                              command=self.evento_btn_eliminar_habito,
                                              font= estilos.FUENTE_SUBTITULOS,
                                              )
        self.boton_eliminar_hab.pack(
            side="left",
            fill="x",
            expand=True,
            padx= estilos.PADX,
            pady = estilos.PADY,
        )
        self.boton_rend_mens =ctk.CTkButton(self.frame_nav,
                                              command=self.evento_grafica_mensual,
                                              text= "Rendimiento Mensual",
                                              font= estilos.FUENTE_SUBTITULOS,
                                              )
        self.boton_rend_mens.pack(
            side="left",
            fill="x",
            expand=True,
            padx= estilos.PADX,
            pady = estilos.PADY,
        )
#---------------------------------------------FRAMES SECUNDARIOS -----------------------------------------------------------------
    def mostrar_frame_encabezado_tabla_2_1 (self):
        #--------------------------------------FRAME 
        self.frame_encabezado = ctk.CTkFrame (
            self.frame_tabla_habitos_contenedor, 
            corner_radius=estilos.CORNER_RADIUS,
            fg_color=estilos.tema_frame_color
            )
        self.frame_encabezado.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(estilos.PADX,estilos.PADX*3.5),
            pady= estilos.PADY
        )
        self.boton_marcar = ctk.CTkButton(
            self.frame_encabezado,
            text="¿Olvidaste marcar ayer?",
            command=self.evento_marcar_ayer,
            #fg_color=estilos.COLOR_CONTRASTE,
            width = self.width_column_habitos_tabla,
            font=estilos.FUENTE_PEQUEÑA)
        self.boton_marcar.grid(
            row=0,
            column=0,
            sticky ="nsew",
            padx=estilos.PADX,
            pady=estilos.PADY
            )
        #Labels dias actuales 
        for indice,dia in enumerate(self.dias_actuales):
            if dia.date()< self.DIA_HOY.date():
                color_label  = estilos.tema_top_frame_color
            elif dia.date() == self.DIA_HOY.date():
                color_label = estilos.tema_botones_color
            elif dia.date() > self.DIA_HOY.date():
                color_label = estilos.tema_progressbar_fondo

            ctk.CTkLabel(self.frame_encabezado,
                         text = dia.day,
                         font=estilos.FUENTE_PEQUEÑA,
                         fg_color=color_label,
                         corner_radius=999
                         ).grid(row=0,
                                column=indice+1,
                                sticky="nsew",
                                padx=1,
                                pady=estilos.PADY
                                )
            self.frame_encabezado.columnconfigure(indice+1, weight = 1,  uniform ="col")
        encabezados = ["Actividad","Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
        for ind,encabezado in enumerate(encabezados): 
            ctk.CTkLabel(self.frame_encabezado,
                         text=encabezado,
                         font=estilos.FUENTE_PEQUEÑA
                         ).grid(
                             row=1,
                             column=ind,
                             sticky="nsew",
                             padx=2,
                             pady=estilos.PADY,

                         )
    def mostrar_frame_marcar_ayer(self):
        self.frame_btn_completar_ayer_contenedor =ctk.CTkFrame(
        self, 
        corner_radius=estilos.CORNER_RADIUS,
        )
        self.frame_btn_completar_ayer_contenedor.grid(
            row=3,
            column=0,
            sticky="nsew",
            rowspan = 3, 
            padx= estilos.PADX,
            pady= estilos.PADY
        )
        
        self.frame_btn_completar_ayer = ctk.CTkScrollableFrame(
            self.frame_btn_completar_ayer_contenedor,
            corner_radius=estilos.CORNER_RADIUS,
            fg_color=estilos.tema_frame_color,
        )
        self.frame_btn_completar_ayer.pack(
            fill="both",
            expand = True,
            padx = estilos.PADX,
            pady = estilos.PADY)
        self.listar_habitos_ayer()
#---------------------------------------------FUNCIONES DE ACTUALIZACION-----------------------------------------------------------
    def actualizar_programa(self):
        print("El programa se ha actualizado")
        self.refrescar_tabla_y_fechas(None)
        self.crear_linea_fecha()
        # Reprogramar la ejecución después de 900,000 ms (15 min)
        self.after(900000, self.actualizar_programa)
    
    def refrescar_tabla_y_fechas(self,event):
        self.inicializar_variables_fechas()
        self.barra_rendimiento.set(self.rendimiento_semanal/100)
        self.label_rendimiento.configure(text =f"{self.rendimiento_semanal}%")
        # Actualizar label del control de semana
        self.label_f_control.configure(text =self.encabezados[1])
        # Redibujar los encabezados y tabla de hábitos
        self.mostrar_frame_encabezado_tabla_2_1()
        self.lista_habitos_frame_semana()
#-------------------------------------------------------EVENTOS--------------------------------------------------------------------
    def evento_semana_anterior(self):
        self.fechas_objeto.semana_anterior()
        self.refrescar_tabla_y_fechas(None)
        
    def evento_semana_siguiente(self):
        self.fechas_objeto.semana_siguiente()
        self.refrescar_tabla_y_fechas(None)

    def evento_marcar_habito(self,nombre_habito): 
        self.db_objeto.registrar_ejecucion_habito(nombre_habito)
        self.rendimiento_semanal = self.fechas_objeto.calcular_rendimiento_semanal()
        self.refrescar_tabla_y_fechas(None)
                # Actualizar botón: cambiar texto y deshabilitar
        if hasattr(self, "botones_habitos") and nombre_habito in self.botones_habitos:
            boton = self.botones_habitos[nombre_habito]
            boton.configure(text=f"{nombre_habito} - Completado!", state="disabled")

    def evento_marcar_habito_ayer(self,nombre_habito): 
        self.db_objeto.registrar_ejecucion_habito_ayer(nombre_habito)
        self.rendimiento_semanal = self.fechas_objeto.calcular_rendimiento_semanal()
        self.refrescar_tabla_y_fechas(None)
                # Actualizar botón: cambiar texto y deshabilitar
        if hasattr(self, "botones_habitos") and nombre_habito in self.botones_habitos:
            boton = self.botones_habitos[nombre_habito]
            boton.configure(text=f"{nombre_habito} - Completado!", state="disabled")
    def evento_btn_agregar_habito(self):
        self.ventana_agregar_habito.crear_frame_derecho()
        self.ventana_agregar_habito.nombre_ventana_frame_1_0()
        for frame in self.ventana_agregar_habito.frames_agregar_habito:
            frame.tkraise()

    def evento_btn_eliminar_habito(self): 
        self.estado_boton_eliminar_habito = not self.estado_boton_eliminar_habito 
        if self.estado_boton_eliminar_habito:
            self.obj_eliminar_habito.frame_eliminar_habito_contenedor.tkraise()
        else: 
            self.frame_btn_completar_contenedor.tkraise()
    def evento_cambiar_tema(self,nuevo_tema=None,nuevo_modo =None):
        msg = CTkMessagebox(
        master = self ,
        title="Confirmación",
        message=f"¿Estás seguro de que deseas cambiar el tema a '{nuevo_tema}'? \n es necesario reiniciar la aplicación",
        font =estilos.FUENTE_PEQUEÑA,
        icon="question", option_1="No", option_2="Sí")
        response =  msg.get()
        if response == "Sí":
            self.guardar_configuracion_tema(nuevo_tema=nuevo_tema)
            self.reiniciar_app()

    def evento_agregar_frase(self):
        self.ventana_agregar_frase_objeto = VentanaAgregarFrase(master=self,db_objeto=self.db_objeto, fecha_objeto= self.fechas_objeto)
    
    def evento_ventana_fuente(self):
        self.fuente_objeto = VentanaFuente(master=self)
    def evento_acerca_de_ventana(self): 
        self.acerca_de_objeto = VentanaAcercaDe(self)
    def evento_grafica_mensual(self):

        #Configurar botones para cambiar entre meses 
        self.configurar_controles_mes()
        #Cambia el encabezado del frame control
        self.label_f_control.configure(text=self.fechas_objeto.encabezado_mes())
        #Calcula el rendimiento que ira en la barra 
        self.promedio_mes = self.fechas_objeto.calcular_rend_mes()
        #Configura la barra con el rendimiento mensual 
        self.barra_rendimiento.set(self.promedio_mes/100)
        self.label_rendimiento.configure(text =f"{self.promedio_mes}%")
        # Muestra el frame de la grafica mensual
        self.frames_ventana_grafica()
        self.obj_ventana_grafica_mes.frame_botones_navegacion.tkraise()

    def evento_mes_anterior(self):

                # Si ya existe una gráfica previa, destruirla
        if hasattr(self.obj_ventana_grafica_mes, "frame_grafica_mensual") and self.obj_ventana_grafica_mes.frame_grafica_mensual:
            self.obj_ventana_grafica_mes.frame_grafica_mensual.destroy()
            self.obj_ventana_grafica_mes.frame_grafica_mensual = None
            self.obj_ventana_grafica_mes.canvas_grafica = None
        # Cambia la fecha a un mes anterior
        self.fechas_objeto.mes_anterior()
        # Recalcula las fechas para hacer los calculos
        self.inicializar_variables_fechas()
        # calcula el rendimiento mensual total para ponerlo en la barra de progreso
        self.promedio_mes = self.fechas_objeto.calcular_rend_mes()
        #Cambia el encabezado del frame control
        self.label_f_control.configure(text=self.fechas_objeto.encabezado_mes())
        #Configura la barra con el rendimiento mensual 
        self.barra_rendimiento.set(self.promedio_mes/100)
        self.label_rendimiento.configure(text =f"{self.promedio_mes}%")
        # Muestra el frame de la grafica mensual
        self.frames_ventana_grafica()

    def evento_mes_siguiente(self):

                # Si ya existe una gráfica previa, destruirla
        if hasattr(self.obj_ventana_grafica_mes, "frame_grafica_mensual") and self.obj_ventana_grafica_mes.frame_grafica_mensual:
            self.obj_ventana_grafica_mes.frame_grafica_mensual.destroy()
            self.obj_ventana_grafica_mes.frame_grafica_mensual = None
            self.obj_ventana_grafica_mes.canvas_grafica = None

        self.fechas_objeto.mes_siguiente()
        self.inicializar_variables_fechas()
        # calcula el rendimiento mensual total para ponerlo en la barra de progreso
        self.promedio_mes = self.fechas_objeto.calcular_rend_mes()
        #Cambia el encabezado del frame control
        self.label_f_control.configure(text=self.fechas_objeto.encabezado_mes())
        #Configura la barra con el rendimiento mensual 
        self.barra_rendimiento.set(self.promedio_mes/100)
        self.label_rendimiento.configure(text =f"{self.promedio_mes}%")
        # Muestra el frame de la grafica mensual
        self.frames_ventana_grafica()

    def evento_marcar_ayer(self):
        
        self.estado_boton_marcar_ayer = not self.estado_boton_marcar_ayer
        if self.estado_boton_marcar_ayer:
            self.frame_btn_completar_ayer_contenedor.tkraise()
            self.fecha_hoy_label.configure(text = self.encabezados[4])
        else: 
            self.fecha_hoy_label.configure(text = self.encabezados[0])
            self.frame_btn_completar_contenedor.tkraise()
            
    def evento_anio_anterior(self):
                        # Si ya existe una gráfica previa, destruirla
        if hasattr(self.grafica_anio_objeto, "frame_grafica_anual") and self.grafica_anio_objeto.frame_grafica_anual:
            self.grafica_anio_objeto.frame_grafica_anual.destroy()
            self.grafica_anio_objeto.frame_grafica_anual = None
            self.grafica_anio_objeto.canvas_grafica = None
        #actualiza la fecha 
        self.fechas_objeto.anio_anterior()
        self.inicializar_variables_fechas()
        #calcular rendimientos de nuevo 
        rend = self.fechas_objeto.rendimiento_meses_anio()
        #Cambia el encabezado del frame control
        self.label_f_control.configure(text=self.fechas_objeto.encabezado_anio())
        #setear barra de progrreso
        self.barra_rendimiento.set(rend[1]/100)
        self.label_rendimiento.configure(text =f"{rend[1]}%")
        self.frames_ventana_grafica_anio()

    def evento_anio_siguiente(self):
        # Si ya existe una gráfica previa, destruirla
        
        if hasattr(self.grafica_anio_objeto, "frame_grafica_anual") and self.grafica_anio_objeto.frame_grafica_anual:
            self.grafica_anio_objeto.frame_grafica_anual.destroy()
            self.grafica_anio_objeto.frame_grafica_anual = None
            self.grafica_anio_objeto.canvas_grafica = None

            
                #actualiza la fecha 
        self.fechas_objeto.anio_siguiente()
        self.inicializar_variables_fechas()
        #calcular rendimientos de nuevo 
        rend = self.fechas_objeto.rendimiento_meses_anio()
        #Cambia el encabezado del frame control
        self.label_f_control.configure(text=self.fechas_objeto.encabezado_anio())
        #setear barra de progrreso
        self.barra_rendimiento.set(rend[1]/100)
        self.label_rendimiento.configure(text =f"{rend[1]}%")
        self.frames_ventana_grafica_anio()
#------------------------------Configura los botones para navegar entre semanas---------------------------------------------------
    def listar_habitos_ayer(self):   
        """Lista los nombres de los hábitos en el marco, agregando solo los nuevos y eliminando los que ya no existan."""

        if not hasattr(self, "habitos_creados_ayer"):
            self.habitos_creados_ayer = set()
        if not hasattr(self, "botones_habitos_ayer"):
            self.botones_habitos_ayer = {}

        ejecuciones = self.db_objeto.cargar_ejecuciones()  # Cargar ejecuciones actuales

        # 1️⃣ Eliminar botones de hábitos que ya no estén en la base de datos
        habitos_actuales = {habit["nombre_habito"] for habit in self.db_objeto.habitos}
        for nombre in list(self.habitos_creados_ayer):
            if nombre not in habitos_actuales:
                if nombre in self.botones_habitos_ayer:
                    self.botones_habitos_ayer[nombre].destroy()
                    del self.botones_habitos_ayer[nombre]
                self.habitos_creados_ayer.remove(nombre)

        # 2️⃣ Si no hay hábitos
        if not self.db_objeto.habitos:
            if not self.habitos_creados_ayer:
                if not hasattr(self, "mensaje_no_habitos"):
                    self.mensaje_no_habitos_ayer = ctk.CTkLabel(
                        self.frame_btn_completar_ayer,
                        text="No hay hábitos registrados.",
                        fg_color=estilos.tema_frame_color,
                        text_color=estilos.COLOR_BORDE,
                        font=estilos.FUENTE_PEQUEÑA
                    )
                    self.mensaje_no_habitos_ayer.pack(pady=5)
            return
        else:
            # Eliminar mensaje de "No hay hábitos" si ahora sí hay
            if hasattr(self, "mensaje_no_habitos_ayer"):
                self.mensaje_no_habitos_ayer.destroy()
                del self.mensaje_no_habitos_ayer

        # 3️⃣ Crear título si no existe
        if not getattr(self, "titulo_habitos_ayer", None):
            self.titulo_habitos_ayer = ctk.CTkLabel(
                self.frame_btn_completar_ayer,
                text="Selecciona el hábito para completarlo!",
                text_color=estilos.COLOR_BORDE,
                font=estilos.FUENTE_PEQUEÑA
            )
            self.titulo_habitos_ayer.pack(pady=5)
        if not getattr(self, "titulo_habitos_ayer_2", None):
            self.titulo_habitos_ayer_2 = ctk.CTkLabel(
                self.frame_btn_completar_ayer,
                text="(Recuerda que esto marcará los hábitos la fecha de ayer)",
                text_color=estilos.COLOR_AUTOR,
                font=estilos.FUENTE_PEQUEÑA
            )
            self.titulo_habitos_ayer_2.pack(pady=5)

        # 4️⃣ Crear botones solo para nuevos hábitos
        for habit in self.db_objeto.habitos:
            nombre = habit["nombre_habito"]
            if nombre not in self.habitos_creados_ayer:
                boton = ctk.CTkButton(
                    self.frame_btn_completar_ayer,
                    text=nombre,
                    fg_color=habit["color"],
                    text_color=estilos.COLOR_BORDE,
                    font=estilos.FUENTE_PEQUEÑA,
                    command=lambda h=nombre: self.evento_marcar_habito_ayer(h)
                )
                boton.pack(fill="x", pady=1, padx=2)

                self.botones_habitos_ayer[nombre] = boton

                # 5️⃣ Verificar si el hábito está completado hoy
                fecha_ayer_str = self.fechas_objeto.DIA_AYER.strftime("%Y-%m-%d")
                completado = any(
                    e["nombre_habito"] == nombre and 
                    e["fecha_ejecucion"] == fecha_ayer_str and 
                    e.get("completado", False) 
                    for e in ejecuciones
                )
                if completado:
                    boton.configure(text=f"{nombre} - Completado!", state="disabled")

                self.habitos_creados_ayer.add(nombre)

    def listar_habitos(self):   
        """Lista los nombres de los hábitos en el marco, agregando solo los nuevos y eliminando los que ya no existan."""

        if not hasattr(self, "habitos_creados"):
            self.habitos_creados = set()
        if not hasattr(self, "botones_habitos"):
            self.botones_habitos = {}

        ejecuciones = self.db_objeto.cargar_ejecuciones()  # Cargar ejecuciones actuales

        # 1️⃣ Eliminar botones de hábitos que ya no estén en la base de datos
        habitos_actuales = {habit["nombre_habito"] for habit in self.db_objeto.habitos}
        for nombre in list(self.habitos_creados):
            if nombre not in habitos_actuales:
                if nombre in self.botones_habitos:
                    self.botones_habitos[nombre].destroy()
                    del self.botones_habitos[nombre]
                self.habitos_creados.remove(nombre)

        # 2️⃣ Si no hay hábitos
        if not self.db_objeto.habitos:
            if not self.habitos_creados:
                if not hasattr(self, "mensaje_no_habitos"):
                    self.mensaje_no_habitos = ctk.CTkLabel(
                        self.frame_btn_completar,
                        text="No hay hábitos registrados.",
                        fg_color=estilos.tema_frame_color,
                        text_color=estilos.COLOR_BORDE,
                        font=estilos.FUENTE_PEQUEÑA
                    )
                    self.mensaje_no_habitos.pack(pady=5)
            return
        else:
            # Eliminar mensaje de "No hay hábitos" si ahora sí hay
            if hasattr(self, "mensaje_no_habitos"):
                self.mensaje_no_habitos.destroy()
                del self.mensaje_no_habitos

        # 3️⃣ Crear título si no existe
        if not getattr(self, "titulo_habitos", None):
            self.titulo_habitos = ctk.CTkLabel(
                self.frame_btn_completar,
                text="Selecciona el hábito para completarlo!",
                text_color=estilos.COLOR_BORDE,
                font=estilos.FUENTE_PEQUEÑA
            )
            self.titulo_habitos.pack(pady=5)

        # 4️⃣ Crear botones solo para nuevos hábitos
        for habit in self.db_objeto.habitos:
            nombre = habit["nombre_habito"]
            if nombre not in self.habitos_creados:
                boton = ctk.CTkButton(
                    self.frame_btn_completar,
                    text=nombre,
                    fg_color=habit["color"],
                    text_color=estilos.COLOR_BORDE,
                    font=estilos.FUENTE_PEQUEÑA,
                    command=lambda h=nombre: self.evento_marcar_habito(h)
                )
                boton.pack(fill="x", pady=1, padx=2)

                self.botones_habitos[nombre] = boton

                # 5️⃣ Verificar si el hábito está completado hoy
                fecha_hoy_str = self.fechas_objeto.DIA_HOY.strftime("%Y-%m-%d")
                completado = any(
                    e["nombre_habito"] == nombre and 
                    e["fecha_ejecucion"] == fecha_hoy_str and 
                    e.get("completado", False) 
                    for e in ejecuciones
                )
                if completado:
                    boton.configure(text=f"{nombre} - Completado!", state="disabled")

                self.habitos_creados.add(nombre)

    def lista_habitos_frame_semana(self):
        # Recargar datos actualizados
        self.db_objeto.cargar_habitos()
        ejecuciones = self.db_objeto.cargar_ejecuciones()

        # --- Mensaje si no hay hábitos ---
        if not self.db_objeto.habitos:
            if not hasattr(self, "label_mensaje_sin_habitos"):
                self.label_mensaje_sin_habitos = ctk.CTkLabel(
                    self.frame_tabla_habitos,
                    text="Crea un nuevo hábito para comenzar! 😏",
                    font=estilos.FUENTE_PEQUEÑA
                )
                self.label_mensaje_sin_habitos.pack(side="top")
            # No seguimos dibujando nada si no hay hábitos
            return
        else:
            if hasattr(self, "label_mensaje_sin_habitos"):
                self.label_mensaje_sin_habitos.destroy()
                del self.label_mensaje_sin_habitos

        # --- Inicializar diccionarios si no existen ---
        if not hasattr(self, "labels_estado_habitos"):
            self.labels_estado_habitos = {}  # {(nombre, dia_indic): etiqueta}
        if not hasattr(self, "labels_nombres_habitos"):
            self.labels_nombres_habitos = {}  # {nombre: etiqueta}

        # --- Crear/actualizar tabla de hábitos ---
        for indic, habit in enumerate(self.db_objeto.habitos):
            nombre = habit["nombre_habito"]
            fecha_creacion = datetime.strptime(habit["Fecha_creacion"], "%Y-%m-%d").date()

            # Crear nombre de hábito si no existe
            if nombre not in self.labels_nombres_habitos:
                label_nombre = ctk.CTkLabel(
                    self.frame_tabla_habitos,
                    text=nombre,
                    #text_color=estilos.COLOR_BORDE,
                    font=estilos.FUENTE_PEQUEÑA,
                    fg_color=estilos.tema_top_frame_color,
                    width=self.width_column_habitos_tabla,
                )
                label_nombre.grid(column=0, row=indic + 1, padx=1, sticky="nsew")
                self.labels_nombres_habitos[nombre] = label_nombre

            # Procesar días
            for dia_indic in range(7):
                dia_semana = self.inicio_semana + timedelta(days=dia_indic)
                dia_semana_str = dia_semana.strftime("%Y-%m-%d")
                dia_ejecucion = habit["dias_ejecucion"][dia_indic]

                # Determinar icono y color
                if dia_semana.date() < fecha_creacion:
                    texto, color_texto = "➖", estilos.COLOR_BORDE
                elif not dia_ejecucion:
                    texto, color_texto = "➖", estilos.COLOR_BORDE
                else:
                    ejecucion = next(
                        (e for e in ejecuciones if e["nombre_habito"] == nombre and e["fecha_ejecucion"] == dia_semana_str),
                        None
                    )
                    if dia_semana.date() == fecha_creacion:
                        if ejecucion:
                            texto = "⭐"
                            color_texto = "green" if ejecucion["completado"] else "red"
                        elif dia_semana.date() < self.fechas_objeto.DIA_HOY.date():
                            # Ya pasó la fecha y no se ejecutó -> rojo
                            texto, color_texto = "⭐", "red"
                        else:
                            texto, color_texto = "⭐", "white"
                    else:
                        if ejecucion:
                            if ejecucion["completado"]:
                                texto, color_texto = "✔", "green"
                            else:
                                texto, color_texto = "✖", "red"
                        else:
                            if dia_semana.date() >= self.fechas_objeto.DIA_HOY.date():
                                texto, color_texto = "", estilos.COLOR_BORDE
                            else:
                                texto, color_texto = "✖", "red"

                key = (nombre, dia_indic)

                if key in self.labels_estado_habitos:
                    # Actualizar si ya existe
                    self.labels_estado_habitos[key].configure(text=texto, text_color=color_texto)
                else:
                    # Crear si no existe
                    label_estado = ctk.CTkLabel(
                        self.frame_tabla_habitos,
                        text=texto,
                        text_color=color_texto,
                        fg_color=estilos.tema_top_frame_color,
                    )
                    label_estado.grid(column=dia_indic + 1, row=indic + 1, padx=1, sticky="nsew")
                    self.labels_estado_habitos[key] = label_estado

    def config_frame_semana(self): 
        for column  in range (1,8): 
            self.frame_tabla_habitos.columnconfigure(column, weight=1,uniform="col")

    def actualizacion_agregar_habito(self):
        self.listar_habitos()
        self.refrescar_tabla_y_fechas(None)

    def configurar_controles_semanales(self): 
        self.boton_der_control.configure(command=self.evento_semana_siguiente)
        self.boton_izq_control.configure(command= self.evento_semana_anterior)

    def reiniciar_app(self):
        self.destroy()  # Cierra la ventana
        os.execl(sys.executable, sys.executable, *sys.argv)

    def cargar_configuracion(self):
        """Carga el tema y modo de apariencia desde configuracion.json o crea el archivo con valores por defecto."""
        tema_por_defecto = "blue"   # Tema default CTk
        modo_por_defecto = "dark"   # Modo default CTk
        fuente_por_defecto = "Comic Sans MS"
        if not os.path.exists(resource_path(config_path)):
            self.TEMA_SELECCIONADO = tema_por_defecto
            self.MODO_APARIENCIA = modo_por_defecto
            self.guardar_configuracion_tema(tema_por_defecto)
            self.guardar_configuracion_fondo(modo_por_defecto)
        else:
            with open(resource_path(config_path), "r") as f:
                config = json.load(f)
                self.TEMA_SELECCIONADO = config.get("TEMA_SELECCIONADO", tema_por_defecto)
                self.MODO_APARIENCIA = config.get("MODO_APARIENCIA", modo_por_defecto)

        # ✅ Aplicar al GUI después de cargar
        if "\\" in self.TEMA_SELECCIONADO: 
            
            ctk.set_default_color_theme(resource_path(self.TEMA_SELECCIONADO))
            ctk.set_appearance_mode(self.MODO_APARIENCIA)
        else:
            print(self.TEMA_SELECCIONADO)
            ctk.set_default_color_theme(self.TEMA_SELECCIONADO)
            ctk.set_appearance_mode(self.MODO_APARIENCIA)

    def guardar_configuracion_tema(self, nuevo_tema = None):
        """Guarda el tema y modo de apariencia en el archivo JSON y los aplica."""
        if nuevo_tema in estilos.TEMAS_COLOR_DEFAULT:
            self.TEMA_SELECCIONADO = nuevo_tema
            ctk.set_default_color_theme(nuevo_tema)
        elif nuevo_tema in estilos.TEMAS_PERSONALIZADOS:
            self.TEMA_SELECCIONADO = f"temas\\{nuevo_tema}.json"
            
            ctk.set_default_color_theme(resource_path(self.TEMA_SELECCIONADO))
            
  
        with open(resource_path(config_path), "w") as f:
            json.dump({
                "TEMA_SELECCIONADO": self.TEMA_SELECCIONADO,
                "MODO_APARIENCIA": self.MODO_APARIENCIA,
                "FUENTE": estilos.FUENTE_PRINCIPAL,
            }, f, indent=4)

    def guardar_configuracion_fondo(self, nuevo_modo): 
        if nuevo_modo:
            self.MODO_APARIENCIA = nuevo_modo
            ctk.set_appearance_mode(nuevo_modo)

        with open(resource_path(config_path), "w") as f:
            json.dump({
                "TEMA_SELECCIONADO": self.TEMA_SELECCIONADO,
                "MODO_APARIENCIA": self.MODO_APARIENCIA,
                "FUENTE": estilos.FUENTE_PRINCIPAL,
            }, f, indent=4)

    def guardar_configuracion_fuente(self, nueva_fuente): 


        with open(resource_path(config_path), "w") as f:
            json.dump({
                "TEMA_SELECCIONADO": self.TEMA_SELECCIONADO,
                "MODO_APARIENCIA": self.MODO_APARIENCIA,
                "FUENTE": nueva_fuente,
            }, f, indent=4)


    def generar_menu_frases(self):
    
        self.set_frases = set()  # Crear set vacío
        for frase in self.db_objeto.frases:
            self.set_frases.add(frase)  # Agrega solo frases únicas

        # Limpiar menú antes de agregar para evitar duplicados al regenerar
        self.submenu_eliminar_frase.clean() 
        

        # Agregar opciones únicas al menú
        for frase_unica in self.set_frases:
            self.submenu_eliminar_frase.add_option(
                option=frase_unica, 
                command= lambda f = frase_unica :self.db_objeto.evento_eliminar_frase_selec(f))
            
    def configurar_controles_mes(self):
        self.boton_izq_control.configure(command = self.evento_mes_anterior)
        self.boton_der_control.configure(command = self.evento_mes_siguiente)

    def configurar_controles_año(self):
        self.boton_izq_control.configure(command = self.evento_anio_anterior)
        self.boton_der_control.configure(command = self.evento_anio_siguiente)
