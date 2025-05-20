import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from .tabla import Tabla

class Interfaz():

    def __init__(self):
        titulos = ['Identificador', 'Nombre', 'Correo Electronico', 'Número Celular', 'Pin']
        columnas = ['id', 'nombre', 'correo', 'telefono','pin']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)
        pass        
            
    def accion_guardar_boton(self, id, nombre, correo, telefono,pin):
        if id == '':
            self.comunicacion.guardar(nombre, correo, telefono,pin)
            
        else:
            self.comunicacion.actualizar(id, nombre, correo, telefono,pin)

    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)

        if resultado:
            texto = "Nombre: " + resultado.get('nombre', '') + \
                ", Correo: " + resultado.get('correo', '') + \
                ", Teléfono: " + resultado.get('telefono', '') + \
                ", PIN: " + resultado.get('pin', '')
        else:
            texto = "Usuario no encontrado."

        labelConsulta.config(text=texto)


    def accion_consultar_todo(self, nombre, correo, telefono,pin):
        resultado = self.comunicacion.consultar_todo(nombre, correo,telefono,pin)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('correo'), elemento.get('telefono'), elemento.get('pin')))
        self.tabla.refrescar(data)
        print(data)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)
        labelNombre = tk.Label(self.ventanaPrincipal, text="Nombre")
        entryNombre = tk.Entry(self.ventanaPrincipal, textvariable=usuario.nombre)
        labelCorreo = tk.Label(self.ventanaPrincipal, text="Correo Electronico")
        entryCorreo = tk.Entry(self.ventanaPrincipal, textvariable=usuario.correo)
        labelTelefono= tk.Label(self.ventanaPrincipal, text="Numero Celular")
        entryTelefono= tk.Entry(self.ventanaPrincipal, textvariable=usuario.telefono)
        labelPin= tk.Label(self.ventanaPrincipal, text="Pin")
        entryPin= tk.Entry(self.ventanaPrincipal, textvariable=usuario.pin)
        
        labelConsulta = tk.Label(self.ventanaPrincipal, text='')
        
        
    
        boton_guardar = tk.Button(self.ventanaPrincipal, 
                   text="Guardar", 
                   command=lambda: self.accion_guardar_boton(entryId.get(), entryNombre.get(), entryCorreo.get(), entryTelefono.get(), entryPin.get()))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, 
                   text="Consultar 1", 
                   command=lambda: self.accion_consultar_boton(labelConsulta, entryId.get()))
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, 
                   text="Consultar todos", 
                   command=lambda: self.accion_consultar_todo(entryNombre.get(), entryCorreo.get(), entryTelefono.get(),entryPin.get()))

        #creando la ventana
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("1000x1000")
        labelId.pack()
        entryId.pack()
        labelNombre.pack()
        entryNombre.pack()
        labelCorreo.pack()
        entryCorreo.pack()
        labelTelefono.pack()
        entryTelefono.pack()
        labelPin.pack()
        entryPin.pack()
        boton_guardar.pack()
        boton_consultar_1.pack()
        boton_consultar_todos.pack()
        labelConsulta.pack()
        self.tabla.tabla.pack()

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                entryNombre.delete(0, tk.END)
                entryNombre.insert(0, str(valores[1]))
                entryCorreo.delete(0, tk.END)
                entryCorreo.insert(0, str(valores[2]))
                entryTelefono.delete(0, tk.END)
                entryTelefono.insert(0, str(valores[3]))
                entryPin.delete(0, tk.END)
                entryPin.insert(0, str(valores[3]))
                

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()