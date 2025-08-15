# pip install customtkinter
import customtkinter as ctk

FRASE = "Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un hábito."
AUTOR = "— (Paráfrasis de ideas de Aristóteles, formulada por Will Durant)"

def main():
    ctk.set_appearance_mode("system")     # "light", "dark" o "system"
    ctk.set_default_color_theme("blue")   # "blue", "dark-blue", "green"

    app = ctk.CTk()
    app.title("Frase inspiradora")
    app.geometry("720x320")
    app.minsize(520, 260)

    # ---------- contenedor principal (centra contenido) ----------
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    wrapper = ctk.CTkFrame(app, corner_radius=20, fg_color=("white", "#1f1f1f"))
    wrapper.grid(row=0, column=0, padx=24, pady=24, sticky="nsew")

    wrapper.grid_rowconfigure(0, weight=1)
    wrapper.grid_columnconfigure(0, weight=1)

    # ---------- encabezado ----------
    titulo = ctk.CTkLabel(
        wrapper,
        text="Frase del día",
        font=("Segoe UI Semibold", 22)
    )
    titulo.grid(row=0, column=0, padx=18, pady=(18, 4), sticky="n")

    # ---------- frase ----------
    label_frase = ctk.CTkLabel(
        wrapper,
        text=f"“{FRASE}”",
        justify="center",
        wraplength=620,              # ajusta el ancho del texto
        font=("Segoe UI", 18)
    )
    label_frase.grid(row=1, column=0, padx=28, pady=(8, 2), sticky="n")

    # ---------- autor ----------
    label_autor = ctk.CTkLabel(
        wrapper,
        text=AUTOR,
        font=("Segoe UI Italic", 14),
        text_color=("gray20", "gray70")
    )
    label_autor.grid(row=2, column=0, padx=18, pady=(0, 16), sticky="n")

    # ---------- barra inferior con switch de tema ----------
    footer = ctk.CTkFrame(wrapper, fg_color="transparent")
    footer.grid(row=3, column=0, padx=16, pady=(4, 16), sticky="ew")
    footer.grid_columnconfigure(0, weight=1)

    tema_label = ctk.CTkLabel(footer, text="Tema:", font=("Segoe UI", 12))
    tema_label.grid(row=0, column=0, sticky="w")

    switch = ctk.CTkSwitch(
        footer, text="Claro / Oscuro",
        command=lambda: alternar_tema(switch)
    )
    # Coloca el switch acorde al modo actual
    switch.select() if ctk.get_appearance_mode().lower() == "dark" else switch.deselect()
    switch.grid(row=0, column=1, sticky="e")

    app.mainloop()

def alternar_tema(switch: ctk.CTkSwitch):
    # Cambia entre "light" y "dark"
    modo_actual = ctk.get_appearance_mode().lower()
    ctk.set_appearance_mode("light" if modo_actual == "dark" else "dark")

if __name__ == "__main__":
    main()
