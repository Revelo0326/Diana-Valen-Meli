import tkinter as tk
from tkinter.messagebox import askyesno, showinfo, showerror
import requests
import re
from tkinter import *

API_URL = "http://127.0.0.1:8000/api/estudiante/"

def el_usuario_quiere_salir():
    if askyesno('Salir de la aplicación', '¿Seguro que quieres cerrar la aplicación?'):
        ventanaPrincipal.destroy()

def evento_precionar_tecla(event, labelValidacion, entrada, tipo):
    texto_validar = ""
    if tipo == "letras":
        if validar_letras(entrada):
            texto_validar = ""
        else:
            texto_validar = "Solo se permiten letras"
    elif tipo == "numeros":
        if validar_numeros(entrada):
            texto_validar = ""
        else:
            texto_validar = "Solo se permiten números"
    labelValidacion.config(text=texto_validar)

def validar_letras(valor):
    patron = re.compile("^[A-Za-zñÑ ]*$")
    return patron.match(valor.get()) is not None

def validar_numeros(valor):
    patron = re.compile("^[0-9.,]*$")
    return patron.match(valor.get()) is not None

def buscar():
    id_estudiante = entryID.get()
    if id_estudiante:
        response = requests.get(API_URL + id_estudiante + "/")
        if response.status_code == 200:
            data = response.json()
            entryNombre.delete(0, END)
            entryNombre.insert(0, data['nombre'])
            entryEdad.delete(0, END)
            entryEdad.insert(0, str(data['edad']))
            entryCarrera.delete(0, END)
            entryCarrera.insert(0, data['carrera'])
            entryPromedio.delete(0, END)
            entryPromedio.insert(0, str(data['promedio']))
            showinfo("Encontrado", f"Estudiante con ID {id_estudiante} encontrado")
        else:
            showerror("Error", "Cliente no encontrado")
            limpiar_campos()

def guardar(nombre, edad, carrera, promedio):
    data = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        showinfo("Éxito", "Cliente guardado correctamente")
    else:
        showerror("Error", "No se pudo guardar el cliente")
    limpiar_campos()

def actualizar():
    id_estudiante = entryID.get()
    if id_estudiante:
        data = {
            "nombre": entryNombre.get(),
            "edad": int(entryEdad.get()),
            "carrera": entryCarrera.get(),
            "promedio": float(entryPromedio.get())
        }
        response = requests.put(API_URL + id_estudiante + "/", json=data)
        if response.status_code == 200:
            showinfo("Éxito", "Cliente actualizado correctamente")
        else:
            showerror("Error", "No se pudo actualizar el cliente")
        limpiar_campos()

def eliminar():
    id_estudiante = entryID.get()
    if id_estudiante:
        response = requests.delete(API_URL + id_estudiante + "/")
        if response.status_code == 204:
            showinfo("Éxito", "Cliente eliminado correctamente")
        else:
            showerror("Error", "No se pudo eliminar el cliente")
        limpiar_campos()

def limpiar_campos():
    entryID.delete(0, END)
    entryNombre.delete(0, END)
    entryEdad.delete(0, END)
    entryCarrera.delete(0, END)
    entryPromedio.delete(0, END)

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("450x480")
ventanaPrincipal.title('Gestión de Cliente')

frame = tk.Frame(ventanaPrincipal)
frame.pack(pady=10)

# ID + Botón Buscar
id_estudiante = tk.StringVar()
labelID = tk.Label(frame, text="ID")
entryID = tk.Entry(frame, textvariable=id_estudiante)
btn_buscar = tk.Button(frame, text="Buscar", width=10, command=lambda:buscar())

labelID.grid(row=0, column=0, padx=5, pady=5)
entryID.grid(row=0, column=1, padx=5, pady=5)
btn_buscar.grid(row=0, column=2, padx=5, pady=5)

# Nombre
nombre = tk.StringVar(frame)
labelNombre = tk.Label(frame, text="Nombre")
entryNombre = tk.Entry(frame, textvariable=nombre)
labelValidacionNombre = tk.Label(frame, text="", fg="red")
entryNombre.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionNombre, nombre, "letras"))

labelNombre.grid(row=1, column=0, padx=5, pady=5)
entryNombre.grid(row=1, column=1, padx=5, pady=5)
labelValidacionNombre.grid(row=2, column=1)

# Edad
edad = tk.StringVar(frame)
labelEdad = tk.Label(frame, text="Edad")
entryEdad = tk.Entry(frame, textvariable=edad)
labelValidacionEdad = tk.Label(frame, text="", fg="red")
entryEdad.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionEdad, edad, "numeros"))

labelEdad.grid(row=3, column=0, padx=5, pady=5)
entryEdad.grid(row=3, column=1, padx=5, pady=5)
labelValidacionEdad.grid(row=4, column=1)

# Carrera
carrera = tk.StringVar(frame)
labelCarrera = tk.Label(frame, text="Carrera")
entryCarrera = tk.Entry(frame, textvariable=carrera)
labelValidacionCarrera = tk.Label(frame, text="", fg="red")
entryCarrera.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionCarrera, carrera, "letras"))

labelCarrera.grid(row=5, column=0, padx=5, pady=5)
entryCarrera.grid(row=5, column=1, padx=5, pady=5)
labelValidacionCarrera.grid(row=6, column=1)

# Promedio
promedio = tk.StringVar(frame)
labelPromedio = tk.Label(frame, text="Promedio")
entryPromedio = tk.Entry(frame, textvariable=promedio)
labelValidacionPromedio = tk.Label(frame, text="", fg="red")
entryPromedio.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionPromedio, promedio, "numeros"))

labelPromedio.grid(row=7, column=0, padx=5, pady=5)
entryPromedio.grid(row=7, column=1, padx=5, pady=5)
labelValidacionPromedio.grid(row=8, column=1)

# Botones
frame_botones = tk.Frame(ventanaPrincipal)
frame_botones.pack(pady=15)

btn_guardar = tk.Button(frame_botones, text="Guardar", width=10, command=lambda:guardar(
                                                                                        entryNombre.get(),
                                                                                        entryEdad.get(),
                                                                                        entryCarrera.get(),
                                                                                        entryPromedio.get()))
btn_actualizar = tk.Button(frame_botones, text="Actualizar", width=10, command=lambda:actualizar())
btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=lambda:eliminar())

btn_guardar.grid(row=0, column=0, padx=5)
btn_actualizar.grid(row=0, column=1, padx=5)
btn_eliminar.grid(row=0, column=2, padx=5)

ventanaPrincipal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
ventanaPrincipal.mainloop()
