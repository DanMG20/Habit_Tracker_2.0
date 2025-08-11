import os
import json
from datetime import datetime
from tkinter import messagebox
class Database:
    def __init__(self):
        self.habitos = self.cargar_habitos()
    def cargar_habitos(self):
        if not os.path.exists("json\\Base_de_datos_habitos.json"):
            return []
        with open("json\\Base_de_datos_habitos.json", "r") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                print("Archivo corrupto, voy a reescribir el archivo")
                return []
    # Guarda la información en el archivo JSON
    def guardar_habitos(self):
        with open("json\\Base_de_datos_habitos.json", "w") as archivo:
            json.dump(self.habitos, archivo, indent=4)

    # Función para crear un hábito
    def crear_habito(self,nombre_habito_nuevo, dias_ejecucion,color):
        # Guardar fecha
        fecha_creacion = datetime.now().date()
        fecha_creacion_string = str(fecha_creacion)
        dias_ejecucion_valores = [dia for dia in dias_ejecucion]
        # Verificamos si el hábito ya existe
        for habito in self.habitos:
            if nombre_habito_nuevo == habito["nombre_habito"]:
                print("Este hábito ya existe, intenta con otro nombre.")

                return

        # Si el hábito no existe, lo creamos
        habito = {
            "nombre_habito": nombre_habito_nuevo,
            "dias_ejecucion": dias_ejecucion_valores,
            "Fecha_creacion": fecha_creacion_string,
            "color": color
        }
        self.habitos.append(habito)
        self.guardar_habitos()
        print(f"El hábito '{nombre_habito_nuevo}' ha sido creado con éxito.")

    def eliminar_habito(): 
        pass

#-----------------------------------------------------EJECUCIONES-----------------------------------------
    def cargar_ejecuciones(self):
        if not os.path.exists(("json\\registro_habitos.json")):
            return[]
        try:
            with open('json\\registro_habitos.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_ejecuciones(self,ejecuciones):
        with open('json\\registro_habitos.json', 'w') as f:
            json.dump(ejecuciones, f, indent=4)

    def registrar_ejecucion_habito(self, nombre_habito):
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        ejecuciones = self.cargar_ejecuciones()

        # Verificar si el hábito ya fue registrado hoy
        if any(ejec["nombre_habito"] == nombre_habito and ejec["fecha_ejecucion"] == fecha_actual for ejec in
               ejecuciones):
            messagebox.showinfo("Información", f"El hábito '{nombre_habito}' ya fue completado hoy.")
            return

        # Agregar nuevo registro
        nuevo_registro = {
            "nombre_habito": nombre_habito,
            "fecha_ejecucion": fecha_actual,
            "completado": True
        }
        ejecuciones.append(nuevo_registro)

        # Guardar actualizaciones
        self.guardar_ejecuciones(ejecuciones)
        messagebox.showinfo("Éxito", f"Se registró como completado el hábito '{nombre_habito}' para hoy.")
