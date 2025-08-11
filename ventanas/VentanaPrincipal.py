import customtkinter as ctk 
from PIL import Image, ImageTk
import estilos
from direcciones import obtener_direccion_icono
from ventanas.VentanaAgregarHabito import *
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
        self.DIA_HOY = self.fechas_objeto.DIA_HOY
        self.encabezados= self.fechas_objeto.encabezados_fechas()
        self.inicio_semana = self.fechas_objeto.inicio_semana()
        self.dias_actuales = self.fechas_objeto.dias_actuales()
        print(self.dias_actuales)
        self.width_column_habitos_tabla = 350 
        #-------------------------------------------INICIALIZAR APP-------------------------------------------------------------------
        self.inicializar_frames_constantes()
        self.inicializar_todos_los_frames()
        self.configuracion_grillado()
        #------------------------------------------CONFIG BOTONES -------------------------------------------------------------------
        #self.config_botones_semana()
        #self.actualizar_programa()

        self.ventana_agregar_habito.evento_btn_cancelar()
    
        #------------------------------------------PARA QUE LA VENTANA SE HABRA EN ZOOM-----------------------------------------------
        self.after_idle(lambda: self.state("zoomed"))
                #Guardar posicion de la pantalla al cerrarse 
        self.protocol("WM_DELETE_WINDOW",
             lambda: (guardar_posicion_ventana(self), self.destroy()))
        
        
#---------------------------------------------FUNCIONES DE INICIALIZACION------------------------------------------------------------


    def inicializar_frames_constantes(self):
        self.mostrar_frames_top()
    def frames_ventana_agregar_habito(self):
        self.ventana_agregar_habito = VentanaAgregarHabito(self,self.frames_ventana_principal_lista,self.db_objeto,self.fechas_objeto)
    def inicializar_todos_los_frames(self):
        self.frames_ventana_principal()
        self.frames_ventana_agregar_habito()
        

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
            justify= "center",
            font=estilos.FUENTE_SUBTITULOS,
            )
        frase_label.pack(
            fill="both",
            expand = True,
            padx= estilos.PADX,
            pady= estilos.PADY
            )
        
    def configuracion_grillado(self): 
        #----------------------------------------------PRINCIPAL
        for columna in range(1,2):
            self.columnconfigure(columna, weight=1)
        self.rowconfigure(3, weight=1)
      

#--------------------------------------------------FRAMES PRINCIPALES-----------------------------------------------------------------
    
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
            text =self.encabezados[0],
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
        self.frame_controles = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_controles.grid(
            row = 1,
            column = 2,
            sticky="nsew",
            padx= estilos.PADX,
            pady = estilos.PADY
        )
        self.boton_izq = ctk.CTkButton(
            self.frame_controles,
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
            self.frame_controles,
            text = self.encabezados[1],
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
            self.frame_controles,
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
        self.frame_btn_completar_contenedor =ctk.CTkFrame(
            self, 
            corner_radius=estilos.CORNER_RADIUS,
        )
        self.frame_btn_completar_contenedor.grid(
            row=2,
            column=0,
            sticky="nsew",
            rowspan = 3, 
            padx= estilos.PADX,
            pady= estilos.PADY
        )
        
        self.frame_btn_completar = ctk.CTkScrollableFrame(
            self.frame_btn_completar_contenedor,
            corner_radius=estilos.CORNER_RADIUS
        )
        self.frame_btn_completar.pack(
            fill="both",
            expand = True,
            padx = estilos.PADX,
            pady = estilos.PADY)
        self.listar_habitos()
    
    def mostrar_frame_tabla_habitos_3_1(self):
        self.frame_tabla_habitos_contenedor = ctk.CTkFrame(self,corner_radius=estilos.CORNER_RADIUS)
        self.frame_tabla_habitos_contenedor.grid(row=2,
                                 column=1,
                                 rowspan=2,
                                 columnspan=2,
                                 sticky="nsew",
                                 pady= estilos.PADY,
                                 padx = estilos.PADX
                                 )
            
        self.frame_tabla_habitos  = ctk.CTkScrollableFrame(
            self.frame_tabla_habitos_contenedor, 
            corner_radius=estilos.CORNER_RADIUS)
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
            row=4,
            column=1,
            columnspan =2,
            sticky="nsew",
            padx=estilos.PADX,
            pady=estilos.PADY
        )
        #-------------------------------------------BOTONES-------------------
        self.boton_agregar_hab =ctk.CTkButton(self.frame_nav,
                                              fg_color=estilos.COLOR_CONTRASTE,
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
                                              fg_color=estilos.COLOR_CONTRASTE,
                                              text= "- Eliminar hábito",
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
                                              fg_color=estilos.COLOR_CONTRASTE,
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
        self.frame_encabezado = ctk.CTkFrame (self.frame_tabla_habitos_contenedor, corner_radius=estilos.CORNER_RADIUS)
        self.frame_encabezado.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=estilos.PADX,
            pady= estilos.PADY
        )
        self.boton_marcar = ctk.CTkButton(
            self.frame_encabezado,
            text="¿Olvidaste marcar ayer?",
            fg_color=estilos.COLOR_CONTRASTE,
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
            if dia< self.DIA_HOY.day:
                color_label  = estilos.COLOR_FONDO
            elif dia == self.DIA_HOY.day:
                color_label = estilos.COLOR_CONTRASTE
            elif dia > self.DIA_HOY.day:
                color_label = estilos.COLORES[0] 

            ctk.CTkLabel(self.frame_encabezado,
                         text = dia,
                         font=estilos.FUENTE_PEQUEÑA,
                         fg_color=color_label,
                         corner_radius=999
                         ).grid(row=0,
                                column=indice+1,
                                sticky="nsew",
                                padx=2,
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

    def evento_btn_agregar_habito(self):
        self.ventana_agregar_habito.crear_frame_derecho()
        self.ventana_agregar_habito.nombre_ventana_frame_1_0()
        for frame in self.ventana_agregar_habito.frames_agregar_habito:
            frame.tkraise()
        
        
        


#------------------------------Configura los botones para navegar entre semanas---------------------------------------------------

    
   

    def listar_habitos(self):   
        """Lista los nombres de los hábitos en el marco, agregando solo los nuevos."""

        # Si no existe el set, lo creamos
        if not hasattr(self, "habitos_creados"):
            self.habitos_creados = set()

        if not self.db_objeto.habitos:
            if not self.habitos_creados:  # Solo mostrar mensaje si está vacío
                ctk.CTkLabel(
                    self.frame_btn_completar,
                    text="No hay hábitos registrados.",
                    text_color=estilos.COLOR_BORDE,
                    font=estilos.FUENTE_PEQUEÑA
                ).pack(pady=5)
        else:
            # Agregar etiqueta inicial solo una vez
            if not getattr(self, "titulo_habitos", None):
                self.titulo_habitos = ctk.CTkLabel(
                    self.frame_btn_completar,
                    text="Selecciona el hábito para completarlo!",
                    text_color=estilos.COLOR_BORDE,
                    font=estilos.FUENTE_PEQUEÑA
                )
                self.titulo_habitos.pack(pady=5)

            # Buscar solo los hábitos que aún no están creados
            for habit in self.db_objeto.habitos:
                nombre = habit["nombre_habito"]
                if nombre not in self.habitos_creados:
                    ctk.CTkButton(
                        self.frame_btn_completar,
                        text=nombre,
                        fg_color=habit["color"],
                        text_color=estilos.COLOR_BORDE,
                        font=estilos.FUENTE_PEQUEÑA,
                        command=lambda h=nombre: self.db_objeto.registrar_ejecucion_habito(h)
                    ).pack(fill="x", pady=1, padx=2)

                    # Marcarlo como creado
                    self.habitos_creados.add(nombre)


    def lista_habitos_frame_semana(self):
        """
        Muestra los hábitos junto con los días de la semana sin recrear todo.
        Solo añade los nuevos hábitos que no se han mostrado aún.
        """
        if not hasattr(self, "habitos_renderizados_semana"):
            self.habitos_renderizados_semana = set()

        ejecuciones = self.db_objeto.cargar_ejecuciones()

        # Revisar cada hábito en la base de datos
        for indic, habit in enumerate(self.db_objeto.habitos):
            nombre = habit["nombre_habito"]

            # Saltar si ya fue dibujado
            if nombre in self.habitos_renderizados_semana:
                continue

            fecha_creacion = datetime.strptime(habit["Fecha_creacion"], "%Y-%m-%d").date()

            # Nombre del hábito
            ctk.CTkLabel(
                self.frame_tabla_habitos,
                text=nombre,
                text_color=estilos.COLOR_BORDE,
                font=estilos.FUENTE_PEQUEÑA,
                fg_color=estilos.COLOR_FONDO,
                width=self.width_column_habitos_tabla,
            ).grid(column=0, row=indic + 1, padx=1, sticky="nsew")

            # Días de la semana
            for dia_indic in range(7):
                dia_semana = self.inicio_semana + timedelta(days=dia_indic)
                dia_semana_str = dia_semana.strftime("%Y-%m-%d")
                dia_ejecucion = habit["dias_ejecucion"][dia_indic]

                # Día antes de la creación → siempre "➖"
                if dia_semana.date() < fecha_creacion:
                    texto = "➖"
                    color_texto = estilos.COLOR_BORDE

                # Día en el que no aplica el hábito
                elif dia_ejecucion == False:
                    texto = "➖"
                    color_texto = estilos.COLOR_BORDE

                else:
                    # Buscar si hubo ejecución ese día
                    ejecucion = next(
                        (e for e in ejecuciones
                        if e["nombre_habito"] == nombre
                        and e["fecha_ejecucion"] == dia_semana_str),
                        None
                    )

                    # Día de creación
                    if dia_semana.date() == fecha_creacion:
                        if ejecucion:
                            texto = "⭐"
                            color_texto = "green" if ejecucion["completado"] else "red"
                        else:
                            texto = "⭐"
                            color_texto = "white"

                    # Otros días posteriores
                    else:
                        if ejecucion:
                            if ejecucion["completado"]:
                                texto = "✔"
                                color_texto = "green"
                            else:
                                texto = "✖"
                                color_texto = "red"
                        else:
                            if dia_semana.date() >= self.fechas_objeto.DIA_HOY.date():
                                texto = ""
                                color_texto = estilos.COLOR_BORDE
                            else:
                                texto = "✖"
                                color_texto = "red"

                # Celda
                ctk.CTkLabel(
                    self.frame_tabla_habitos,
                    text=texto,
                    text_color=color_texto,
                    fg_color=estilos.COLOR_FONDO,
                ).grid(column=dia_indic + 1, row=indic + 1, padx=1, sticky="nsew")

            # Guardar como renderizado
            self.habitos_renderizados_semana.add(nombre)

    def config_frame_semana(self): 
        for column  in range (1,8): 
            self.frame_tabla_habitos.columnconfigure(column, weight=1,uniform="col")

    def actualizacion_agregar_habito(self):
        self.listar_habitos()
        self.lista_habitos_frame_semana()

        