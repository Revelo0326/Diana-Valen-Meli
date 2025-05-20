import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.id = tk.StringVar(ventanaPrincipal)
        self.nombre = tk.StringVar(ventanaPrincipal)
        self.edad = tk.StringVar(ventanaPrincipal)
        self.carrera = tk.StringVar(ventanaPrincipal)
        self.promedio = tk.StringVar(ventanaPrincipal)
        