import customtkinter as ctk 
import json
from pathlib import Path
import os
import estilos

direccion_archivo_posicion_ventana  = Path("posicion_ventana.json")

def guardar_posicion_ventana(ventana):
    x = ventana.winfo_x()
    y = ventana.winfo_y()
    datos = {
        "posicion": {"x": x, "y": y},
    }


    with direccion_archivo_posicion_ventana.open("w") as f:
         json.dump(datos, f)
def cargar_posicion_ventana(ventana):
        # Verificar si el archivo existe
        if os.path.exists(direccion_archivo_posicion_ventana):
            with open(direccion_archivo_posicion_ventana, "r") as f:
                datos = json.load(f)
                posicion = datos["posicion"]
                ventana.geometry(f"+{posicion['x']}+{posicion['y']}")
        else:
            # Si no existe el archivo, centrar la ventana
            ventana.update_idletasks()  # Asegura que se obtengan los valores correctos de tamaño
            screen_width = ventana.winfo_screenwidth()
            screen_height = ventana.winfo_screenheight()
            ventana.geometry(
                f"800x600+{(screen_width - 800) // 2}+{(screen_height - 600) // 2}")  # Ajusta el tamaño predeterminado si es necesario



class VentanaComun(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Habit Tracker")
        #Ajustar pantalla
        #cargar_posicion_ventana(self)
        self.geometry("1536x815")
        self.state("zoomed")

        # para dejar que se expandan los frames 
        self.rowconfigure (0, weight= 1)
        self.columnconfigure(0, weight = 1)

        #crear interfaz 
        self.mostrar_frame1()
        self.mostrar_frame2()
        self.mostrar_frame3()
        self.configurar_mayado_frames()

        #Guardar posicion de la pantalla al cerrarse 
        self.protocol("WM_DELETE_WINDOW",
             lambda: (guardar_posicion_ventana(self), self.destroy()))
        
    def mostrar_frame1 (self):
         #Frame1 
         self.frame1 = ctk.CTkFrame(self)
         # configurar expansion del frame
         for fila in range (2): 
            self.frame1.rowconfigure(fila, weight=1)
         for columna in range (3):
            print(columna)
            self.frame1.columnconfigure(columna, weight=1)
         #titulo
         self.tituloapp_label = ctk.CTkLabel(self.frame1, font=estilos.FUENTE_TITULO, text ="HABIT TRACKER")
         self.tituloapp_label.grid(column = 0 , sticky="nsew")
         #frase
         self.frase_label = ctk.CTkLabel(self.frame1, text= "Somos lo que hacemos - Sócrates" )
         self.frase_label.grid(columnspan = 2, column= 2 , sticky= "nsew")
         self.frame1.grid(row = 0,rowspan = 2, sticky = "nsew")
    
    def mostrar_frame2 (self): 
        self.frame2 = ctk.CTkFrame(self)
              # configurar expansion del frame 
        for fila in range (2): 
            self.frame2.rowconfigure(fila, weight=1)

        for columna in range (3):
            print(columna)
            self.frame2.columnconfigure(columna, weight=1)
         #Fecha
        self.fecha_hoy_label = ctk.CTkLabel(self.frame2, text ="Hoy Miércoles 29")
        self.fecha_hoy_label.grid(column = 0 , sticky="nsew")
        #Semana
        self.semana_label= ctk.CTkLabel(self.frame2, text= "Semana 5" )
        self.semana_label.grid(columnspan = 2, column= 2 , sticky= "nsew")
        self.frame2.grid(row = 2, sticky = "nsew",rowspan=2)
    def mostrar_frame3(self): 
        self.frame3 = ctk.CTkFrame(self)
        for fila in range (6):
            self.frame3.rowconfigure(fila, weight =1)
        self.frame3.grid(row = 4, rowspan= 6, sticky= "nsew")

    def configurar_mayado_frames(self):
        #Columnas
        self.frame1.columnconfigure(0, weight=1)
        #Filas
        for fila in range (10):
            print(fila)
            self.frame1.rowconfigure(fila, weight=1)
        #Todavia no termino aqui 




    
    

GUI = VentanaComun()
GUI.mainloop()
