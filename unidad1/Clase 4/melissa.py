import tkinter as tk
import re

texto_validar_usuario = ""
texto_validar_correo = ""
texto_validar_telefono = ""
texto_validar_pin = ""

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("VENTANA PRINCIPAL")
ventanaPrincipal.geometry("300x300")
ventanaPrincipal.configure(bg="#E0F7FA")  

usuario = tk.StringVar()
etiquetaUsuario = tk.Label(ventanaPrincipal, text="Nombre de usuario:", bg="#B2EBF2", fg="#03396C")
entradaUsuario = tk.Entry(ventanaPrincipal, textvariable=usuario, bg="#ABDEE6", fg="#03396C")
etiquetaValidacionUsuario = tk.Label(ventanaPrincipal, text="", bg="#EBF9FD", fg="#005B96")

correo = tk.StringVar()
etiquetaCorreo = tk.Label(ventanaPrincipal, text="Correo electrónico:", bg="#B2EBF2", fg="#03396C")
entradaCorreo = tk.Entry(ventanaPrincipal, textvariable=correo, bg="#ABDEE6", fg="#03396C")
etiquetaValidacionCorreo = tk.Label(ventanaPrincipal, text="", bg="#EBF9FD", fg="#005B96")

telefono = tk.StringVar()
etiquetaTelefono = tk.Label(ventanaPrincipal, text="Número de teléfono:", bg="#B2EBF2", fg="#03396C")
entradaTelefono = tk.Entry(ventanaPrincipal, textvariable=telefono, bg="#ABDEE6", fg="#03396C")
etiquetaValidacionTelefono = tk.Label(ventanaPrincipal, text="", bg="#EBF9FD", fg="#005B96")

pin = tk.StringVar()
etiquetaPin = tk.Label(ventanaPrincipal, text="Pin:", bg="#B2EBF2", fg="#03396C")
entradaPin = tk.Entry(ventanaPrincipal, textvariable=pin, show="*", bg="#ABDEE6", fg="#03396C")
etiquetaValidacionPin = tk.Label(ventanaPrincipal, text="", bg="#EBF9FD", fg="#005B96")


def validarletra(valor):
    patron = re.compile("^[A-Za-zñÑ]*$")
    return patron.match(valor.get()) is not None

def validarNumero(valor):
    patron = re.compile("^[0-9]*$")
    return patron.match(valor.get()) is not None

def evento_presionar_tecla(event):
    global texto_validar_usuario
    global texto_validar_correo
    global texto_validar_telefono
    global texto_validar_pin

    if validarletra(usuario):
        texto_validar_usuario = ""
    else:
        texto_validar_usuario = "Solo se permiten letras"
    etiquetaValidacionUsuario.config(text=texto_validar_usuario)

    if validarletra(correo) or validarNumero(correo):
        texto_validar_correo = ""
    else:
        texto_validar_correo = "Solo letras y números"
    etiquetaValidacionCorreo.config(text=texto_validar_correo)

    if validarNumero(telefono):
        texto_validar_telefono = ""
    else:
        texto_validar_telefono = "Solo se permiten números"
    etiquetaValidacionTelefono.config(text=texto_validar_telefono)

    if validarNumero(pin):
        texto_validar_pin = ""
    else:
        texto_validar_pin = "Solo se permiten números"
    etiquetaValidacionPin.config(text=texto_validar_pin)

etiquetaUsuario.pack()
entradaUsuario.bind("<KeyRelease>", evento_presionar_tecla)
entradaUsuario.pack()
etiquetaValidacionUsuario.pack()

etiquetaCorreo.pack()
entradaCorreo.bind("<KeyRelease>", evento_presionar_tecla)
entradaCorreo.pack()
etiquetaValidacionCorreo.pack()

etiquetaTelefono.pack()
entradaTelefono.bind("<KeyRelease>", evento_presionar_tecla)
entradaTelefono.pack()
etiquetaValidacionTelefono.pack()

etiquetaPin.pack()
entradaPin.bind("<KeyRelease>", evento_presionar_tecla)
entradaPin.pack()
etiquetaValidacionPin.pack()

ventanaPrincipal.mainloop()

