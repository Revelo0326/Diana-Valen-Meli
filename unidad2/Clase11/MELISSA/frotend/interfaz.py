import tkinter as tk
from tkinter.messagebox import askyesno, showinfo, showerror
import requests
import re
from tkinter import *

API_URL = "http://127.0.0.1:8000/api/usuario/"

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

def validar_alfanumerico(texto):
    return re.fullmatch(r'[A-Za-z0-9]*', texto) is not None

def buscar():
    id_usuario = entryID.get()
    if id_usuario:
        response = requests.get(API_URL + id_usuario + "/")
        if response.status_code == 200:
            data = response.json()
            entryNombre.delete(0, END)
            entryNombre.insert(0, data['nombre'])
            entryCorreo.delete(0, END)
            entryCorreo.insert(0, str(data['correo']))
            entryTelefono.delete(0, END)
            entryTelefono.insert(0, data['telefono'])
            entryPin.delete(0, END)
            entryPin.insert(0, str(data['pin']))
            showinfo("Encontrado", f"Estudiante con ID {id_usuario} encontrado")
        else:
            showerror("Error", "Cliente no encontrado")
            limpiar_campos()

def guardar(nombre, correo, telefono, pin):
    data = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono,
        "pin": pin 
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        showinfo("Éxito", "Cliente guardado correctamente")
    else:
        showerror("Error", "No se pudo guardar el cliente")
    limpiar_campos()

def actualizar():
    id_usuario = entryID.get()
    if id_usuario:
        data = {
            "nombre": entryNombre.get(),
            "correo": entryCorreo.get(),
            "telefono": int(entryTelefono.get()),
            "pin":  int(entryPin.get()),
        }
        response = requests.put(API_URL + id_usuario + "/", json=data)
        if response.status_code == 200:
            showinfo("Éxito", "Cliente actualizado correctamente")
        else:
            showerror("Error", "No se pudo actualizar el cliente")
        limpiar_campos()

def eliminar():
    id_usuario = entryID.get()
    if id_usuario:
        response = requests.delete(API_URL + id_usuario + "/")
        if response.status_code == 204:
            showinfo("Éxito", "Cliente eliminado correctamente")
        else:
            showerror("Error", "No se pudo eliminar el cliente")
        limpiar_campos()

def limpiar_campos():
    entryID.delete(0, END)
    entryNombre.delete(0, END)
    entryCorreo.delete(0, END)
    entryTelefono.delete(0, END)
    entryPin.delete(0, END)

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("450x480")
ventanaPrincipal.title('Gestión de Cliente')

frame = tk.Frame(ventanaPrincipal)
frame.pack(pady=10)

# ID + Botón Buscar
id_usuario = tk.StringVar()
labelID = tk.Label(frame, text="ID")
entryID = tk.Entry(frame, textvariable=id_usuario)
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

# Correo
correo = tk.StringVar(frame)
labelCorreo = tk.Label(frame, text="Correo")
entryCorreo = tk.Entry(frame, textvariable=correo)
labelValidacionCorreo = tk.Label(frame, text="", fg="red")
entryCorreo.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionCorreo, correo, "alfanumerico"))

labelCorreo.grid(row=3, column=0, padx=5, pady=5)
entryCorreo.grid(row=3, column=1, padx=5, pady=5)
labelValidacionCorreo.grid(row=4, column=1)

# Telefono
telefono = tk.StringVar(frame)
labelTelefono = tk.Label(frame, text="Telefono")
entryTelefono = tk.Entry(frame, textvariable=telefono)
labelValidacionTelefono = tk.Label(frame, text="", fg="red")
entryTelefono.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionTelefono, telefono, "numeros"))

labelTelefono.grid(row=5, column=0, padx=5, pady=5)
entryTelefono.grid(row=5, column=1, padx=5, pady=5)
labelValidacionTelefono.grid(row=6, column=1)

# Pin
pin = tk.StringVar(frame)
labelPin = tk.Label(frame, text="Pin")
entryPin = tk.Entry(frame, textvariable=pin)
labelValidacionPin = tk.Label(frame, text="", fg="red")
entryPin.bind("<KeyRelease>", lambda event: evento_precionar_tecla(event, labelValidacionPin, pin, "numeros"))

labelPin.grid(row=7, column=0, padx=5, pady=5)
entryPin.grid(row=7, column=1, padx=5, pady=5)
labelValidacionPin.grid(row=8, column=1)

# Botones
frame_botones = tk.Frame(ventanaPrincipal)
frame_botones.pack(pady=15)

btn_guardar = tk.Button(frame_botones, text="Guardar", width=10, command=lambda:guardar(
                                                                                        entryNombre.get(),
                                                                                        entryCorreo.get(),
                                                                                        entryTelefono.get(),
                                                                                        entryPin.get()))
btn_actualizar = tk.Button(frame_botones, text="Actualizar", width=10, command=lambda:actualizar())
btn_eliminar = tk.Button(frame_botones, text="Eliminar", width=10, command=lambda:eliminar())

btn_guardar.grid(row=0, column=0, padx=5)
btn_actualizar.grid(row=0, column=1, padx=5)
btn_eliminar.grid(row=0, column=2, padx=5)

ventanaPrincipal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)
ventanaPrincipal.mainloop()
