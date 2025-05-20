import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.nombre = tk.StringVar(ventanaPrincipal)
        self.correo = tk.StringVar(ventanaPrincipal)
        self.telefono = tk.StringVar(ventanaPrincipal)
        self.pin = tk.StringVar(ventanaPrincipal)
        