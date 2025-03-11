import tkinter as tk
from tkinter.messagebox import askyesno
import re

def el_usuario_quiere_salir():
    if askyesno('salir de la aplicacion', '¿seguro que quieres cerrar la aplicacion'):
        ventanaPrincipal.destroy()

def evento_precionar_tecla(event, labelValidacion, entrada, tipo):
    texto_validar_nombre = ""
    if tipo == "letras":
        if validar_letras(entrada):
            texto_validar_nombre = ""
        else:
            texto_validar_nombre = "Solo se permiten letras"
    elif tipo == "numeros":
        if validar_numeros(entrada):
            texto_validar_nombre = ""
        else:
            texto_validar_nombre = "Solo se permiten números"
    labelValidacion.config(text=texto_validar_nombre)

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    resultado = patron.match(valor.get()) is not None
    return resultado

def validar_numeros(valor):
    patron = re.compile("^[0-9, .]*$")
    resultado = patron.match(valor.get()) is not None
    return resultado

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("300x300")
ventanaPrincipal.title('Estudiante')

frame = tk.Frame(ventanaPrincipal, width=500, height=500)
frame.pack()

nombre = tk.StringVar(ventanaPrincipal)
labelNombre = tk.Label(frame, text="Nombre")
entryNombre = tk.Entry(frame, textvariable=nombre)
labelValidacionNombre = tk.Label(frame, text="", fg="red")
entryNombre.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionNombre, nombre, "letras"))

labelNombre.grid(row=0, column=0)
entryNombre.grid(row=0, column=1)
labelValidacionNombre.grid(row=1, column=1)

edad = tk.StringVar(ventanaPrincipal)
labelEdad = tk.Label(frame, text="Edad")
entryEdad = tk.Entry(frame, textvariable=edad)
labelValidacionEdad = tk.Label(frame, text="", fg="red")
entryEdad.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionEdad, edad, "numeros"))

labelEdad.grid(row=2, column=0)
entryEdad.grid(row=2, column=1)
labelValidacionEdad.grid(row=3, column=1)

carrera = tk.StringVar(ventanaPrincipal)
labelCarrera = tk.Label(frame, text="Carrera")
entryCarrera = tk.Entry(frame, textvariable=carrera)
labelValidacionCarrera = tk.Label(frame, text="", fg="red")
entryCarrera.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionCarrera, carrera, "letras"))

labelCarrera.grid(row=4, column=0)
entryCarrera.grid(row=4, column=1)
labelValidacionCarrera.grid(row=5, column=1)

promedio = tk.StringVar(ventanaPrincipal)
labelPromedio = tk.Label(frame, text="Promedio")
entryPromedio = tk.Entry(frame, textvariable=promedio)
labelValidacionPromedio = tk.Label(frame, text="", fg="red")
entryPromedio.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionPromedio, promedio, "numeros"))

labelPromedio.grid(row=6, column=0)
entryPromedio.grid(row=6, column=1)
labelValidacionPromedio.grid(row=7, column=1)

ventanaPrincipal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
ventanaPrincipal.mainloop()
