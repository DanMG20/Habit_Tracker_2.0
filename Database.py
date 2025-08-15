import os
import json
from datetime import datetime
from CTkMessagebox import CTkMessagebox
import estilos
import shutil
import direcciones
import random
class Database:
    def __init__(self, master):
        self.habitos = self.cargar_habitos()
        self.master = master
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
            CTkMessagebox(master =self.master,
            font =estilos.FUENTE_PEQUEÑA,
            message= ("Información", f"El hábito '{nombre_habito}' ya fue completado hoy."),
            icon="check", option_1="Aceptar")
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
        CTkMessagebox(master =self.master,
                    font =estilos.FUENTE_PEQUEÑA,
                    message= ("Éxito", f"Se registró como completado el hábito '{nombre_habito}' para hoy."),
                    icon="check", option_1="Aceptar")
    


#-------------------------------------RESET--------------------------------

    def resetear_archivos(self): 
        msg = CTkMessagebox(
            master=self.master,
            title="Confirmación",
            message="¿Estás seguro de que deseas restaurar la aplicación? TODOS los archivos y registros serán borrados. Esta acción no se puede deshacer.",
            font=estilos.FUENTE_PEQUEÑA,
            icon="question",
            option_1="No",
            option_2="Sí"
        )
        response = msg.get()

        if response == "Sí":
            direccion = direcciones.obtener_direccion_dir_json()

            try:
                # Borrar TODO el directorio de golpe
                shutil.rmtree(direccion)

                # Volver a crear la carpeta vacía
                os.makedirs(direccion, exist_ok=True)

                # Mensaje de éxito
                CTkMessagebox(
                    master=self.master,
                    title="Información",
                    font=estilos.FUENTE_PEQUEÑA,
                    message="Los registros han sido eliminados. Se reiniciará la aplicación."
                )

                # Reiniciar la app
                self.master.reiniciar_app()

            except Exception as e:
                print(f"No se pudo borrar el directorio {direccion}: {e}")
                CTkMessagebox(
                    master=self.master,
                    title="Error",
                    font=estilos.FUENTE_PEQUEÑA,
                    message=f"No se pudo eliminar los archivos: {e}"
                )

#-----------------------------------------------------FRASES-----------------------------------------
    def cargar_frases_random(self):
        if not os.path.exists("json\\frases.json"):
            frase_default = [{
                "frase": "Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un hábito.",
                "autor": "Aristóteles",
                "indice": 1
            }]
            with open("json\\frases.json", 'w') as f:
                json.dump(frase_default, f, indent=4)

        try:
            with open("json\\frases.json", 'r') as f:
                frases = json.load(f)
                self.frases = []

                for frase in frases:
                    self.frases.append(f"{frase['frase']} - {frase['autor']}") 


            if frases:
                frase_random = random.choice(frases)  # Selección aleatoria
                self.frase_seleccionada = frase_random["frase"]
                self.autor_frase = frase_random["autor"]
                print(self.frase_seleccionada)
                print(self.autor_frase)
            else:
                print("No hay frases registradas.")

        except FileNotFoundError:
            print("KESTAPASANDO")
            

    def evento_eliminar_frase_selec(self, frase_seleccionada):
        """Elimina directamente la frase seleccionada del archivo JSON."""
        msg = CTkMessagebox(
            master=self.master,
            title="Confirmación",
            message=f"¿Estás seguro de que deseas eliminar la frase '{frase_seleccionada}'?",
            font=estilos.FUENTE_PEQUEÑA,
            icon="question", option_1="No", option_2="Sí"
        )
        response = msg.get()

        if response == "Sí":
            ruta_frases = "json\\frases.json"

            # Leer archivo existente
            if os.path.exists(ruta_frases):
                with open(ruta_frases, "r") as f:
                    frases = json.load(f)
            else:
                frases = []

            # Separar frase y autor (porque cargar_frases_random las concatena con " - ")
            if " - " in frase_seleccionada:
                texto_frase, autor = frase_seleccionada.split(" - ", 1)
                frases = [
                    f for f in frases
                    if f["frase"] != texto_frase or f["autor"] != autor
                ]
            else:
                frases = [
                    f for f in frases
                    if f["frase"] != frase_seleccionada
                ]

            # Guardar cambios en el JSON
            with open(ruta_frases, "w") as f:
                json.dump(frases, f, indent=4)

            # Mensaje de confirmación
            CTkMessagebox(
                master=self.master,
                title="Info",
                font=estilos.FUENTE_PEQUEÑA,
                message=f"La frase '{frase_seleccionada}' ha sido eliminada."
            )

            # Recargar frases y regenerar menú
            self.cargar_frases_random()
            self.master.mostrar_frase()
            self.master.generar_menu_frases()
