import customtkinter as ctk
from tkinter import font

class SelectorFuente(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Selector de Fuente")
        self.geometry("400x300")

        self.fuente_seleccionada = "Arial"

        # Label de ejemplo
        self.label = ctk.CTkLabel(self, text="Texto de ejemplo", font=(self.fuente_seleccionada, 20))
        self.label.pack(pady=20)

        # Entry para buscar fuentes
        self.buscar_entry = ctk.CTkEntry(self, placeholder_text="Buscar fuente...")
        self.buscar_entry.pack(pady=5, fill="x", padx=10)
        self.buscar_entry.bind("<KeyRelease>", self.filtrar_fuentes)

        # Obtener todas las fuentes del sistema
        self.fuentes_disponibles = sorted(list(font.families()))

        # ComboBox para elegir fuente
        self.combo_fuente = ctk.CTkComboBox(self, values=self.fuentes_disponibles)
        self.combo_fuente.set(self.fuente_seleccionada)
        self.combo_fuente.pack(pady=10, fill="x", padx=10)

        # Botón para aplicar fuente
        self.btn_aplicar = ctk.CTkButton(self, text="Aplicar Fuente", command=self.aplicar_fuente)
        self.btn_aplicar.pack(pady=10)

    def filtrar_fuentes(self, event):
        texto = self.buscar_entry.get().lower()
        filtradas = [f for f in self.fuentes_disponibles if texto in f.lower()]
        self.combo_fuente.configure(values=filtradas)
        if filtradas:
            self.combo_fuente.set(filtradas[0])

    def aplicar_fuente(self):
        self.fuente_seleccionada = self.combo_fuente.get()
        self.label.configure(font=(self.fuente_seleccionada, 20))
        self.label.configure(text="Texto de ejemplo")  # Restaurar texto original

if __name__ == "__main__":
    app = SelectorFuente()
    app.mainloop()
