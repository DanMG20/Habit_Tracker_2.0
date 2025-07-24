import os
import json
from datetime import datetime
class Database:
    def __init__(self):
        self.habitos = self.cargar_habitos()
    def cargar_habitos(self):
        if not os.path.exists("Base_de_datos_habitos.json"):
            return []
        with open("Base_de_datos_habitos.json", "r") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                print("Archivo corrupto, voy a reescribir el archivo")
                return []
    # Guarda la información en el archivo JSON
    def guardar_habitos(self):
        with open("Base_de_datos_habitos.json", "w") as archivo:
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

