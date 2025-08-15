import json
import os
import estilos
from direcciones import obtener_direccion_icono_top
import customtkinter as ctk
class VentanaAgregarFrase(ctk.CTkToplevel):
    def __init__(self, master,db_objeto,fecha_objeto):
        super().__init__()
        self.master = master
        self.db_objeto = db_objeto
        self.fecha_objeto = fecha_objeto
        self.crear_ventana_crear_frase()


    def crear_ventana_crear_frase(self):
            pantalla_ancho = self.winfo_screenwidth()
            pantalla_alto = self.winfo_screenheight()
            ancho = 500
            alto = 250
            # Calcular coordenadas centradas
            x = (pantalla_ancho // 2) - (ancho // 2) + 143
            print(x)
            y = (pantalla_alto // 2) - (alto // 2)

            print(pantalla_alto)
            print(pantalla_ancho)
            print(x)
            print(y)


            self.geometry(f"{ancho}x{alto}+{x}+{y}")
            # Crear Toplevel
            self.title("Agregar nueva frase")
            self.iconbitmap(obtener_direccion_icono_top())
            ctk.CTkLabel(self,
                        font= estilos.FUENTE_PEQUEÑA,
                        text="Frase:").pack(pady=(10, 0))
            self.entry_frase = ctk.CTkEntry(
                self,
                font=estilos.FUENTE_PEQUEÑA,
                width=350)
            self.entry_frase.pack(pady=5)

            ctk.CTkLabel(self,
                        font=estilos.FUENTE_PEQUEÑA,
                        text="Autor:").pack(pady=(10, 0))
            self.entry_autor = ctk.CTkEntry(self, width=350)
            self.entry_autor.pack(pady=5)

            self.label_error = ctk.CTkLabel(self, 
                                            text="",
                                            font=estilos.FUENTE_PEQUEÑA, 
                                            text_color="red")
            self.label_error.pack(pady=5)

            btn_guardar = ctk.CTkButton(self, 
                                        text="Guardar frase",
                                        font=estilos.FUENTE_PEQUEÑA, 
                                        command=self.guardar_frase)
            btn_guardar.pack(pady=10)

    def guardar_frase(self):
        frase_texto = self.entry_frase.get().strip()
        autor_texto = self.entry_autor.get().strip()

        if not frase_texto or not autor_texto:
            self.label_error.configure(text="Ambos campos son obligatorios")
            return

        # Cargar frases existentes
        ruta_frases = "json\\frases.json"
        if os.path.exists(ruta_frases):
            with open(ruta_frases, "r") as f:
                frases = json.load(f)
        else:
            frases = []

        # Asignar índice secuencial
        if frases:
            ultimo_indice = max(f.get("indice", 0) for f in frases)
        else:
            ultimo_indice = 0
        nuevo_indice = ultimo_indice + 1

        # Crear nuevo objeto frase
        nueva_frase = {
            "frase": frase_texto,
            "autor": autor_texto,
            "indice": nuevo_indice
        }

        frases.append(nueva_frase)

        # Guardar en JSON
        os.makedirs(os.path.dirname(ruta_frases), exist_ok=True)
        with open(ruta_frases, "w") as f:
            json.dump(frases, f, indent=4)

        self.destroy()  # Cerrar ventana
        self.db_objeto.cargar_frases_random()
        self.master.generar_menu_frases()

