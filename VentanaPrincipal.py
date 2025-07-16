import customtkinter as ctk 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter Example")
        self.geometry("400x300")
        self.state("zoomed")
        # Create a button
        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=20)


