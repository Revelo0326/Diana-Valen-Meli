import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from .tabla import Tabla

class Interfaz():

    def __init__(self):
        titulos = ['ID', 'Nombre', 'Edad', 'Carrera', 'Promedio']
        columnas = ['id', 'nombre', 'edad', 'carrera', 'promedio']
        data = []
        self.ventanaPrincipal = tk.Tk()
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.tabla = Tabla(self.ventanaPrincipal, titulos, columnas, data)
        pass

    def accion_guardar_boton(self, id, nombre, edad, carrera, promedio):
        if id == '':
            self.comunicacion.guardar(nombre, edad, carrera, promedio)
        else:
            self.comunicacion.actualizar(id, nombre, edad, carrera, promedio)

    
    def accion_consultar_boton(self, labelConsulta, id):
        resultado = self.comunicacion.consultar(id)
        if resultado:
            labelConsulta.config(text=resultado.get('nombre'))
            data = [(
                resultado.get('id'),
                resultado.get('nombre'),
                resultado.get('edad'),
                resultado.get('carrera'),
                resultado.get('promedio')
            )]
            self.tabla.refrescar(data)
        else:
            labelConsulta.config(text="Estudiante no encontrado.")
            self.tabla.refrescar([]) 

     
    def accion_consultar_todo(self, nombre, edad, carrera, promedio):
        resultado = self.comunicacion.consultar_todo(nombre, edad, carrera, promedio)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('edad'), elemento.get('carrera'), elemento.get('promedio')))
        self.tabla.refrescar(data)
        print(data)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)

        labelId = tk.Label(self.ventanaPrincipal, text="Id")
        entryId = tk.Entry(self.ventanaPrincipal, textvariable=usuario.id)
        labelNombre = tk.Label(self.ventanaPrincipal, text="Nombre")
        entryNombre = tk.Entry(self.ventanaPrincipal, textvariable=usuario.nombre)
        labelEdad = tk.Label(self.ventanaPrincipal, text="Edad")
        entryEdad = tk.Entry(self.ventanaPrincipal, textvariable=usuario.edad)
        labelCarrera = tk.Label(self.ventanaPrincipal, text="Carrera")
        entryCarrera = tk.Entry(self.ventanaPrincipal, textvariable=usuario.carrera)
        labelPromedio = tk.Label(self.ventanaPrincipal, text="Promedio")
        entryPromedio = tk.Entry(self.ventanaPrincipal, textvariable=usuario.promedio)
        labelConsulta = tk.Label(self.ventanaPrincipal, text='')
        
        boton_guardar = tk.Button(self.ventanaPrincipal, 
                   text="Guardar", 
                   command=lambda: self.accion_guardar_boton(entryId.get(), entryNombre.get(), entryEdad.get(), entryCarrera.get(), entryPromedio.get()))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, 
                   text="Consultar 1", 
                   command=lambda: self.accion_consultar_boton(labelConsulta, entryId.get()))
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, 
                   text="Consultar todos", 
                   command=lambda: self.accion_consultar_todo(entryNombre.get(), entryEdad.get(), entryCarrera.get(), entryPromedio.get()))

        #ventana
        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("1000x1000")
        labelId.pack()
        entryId.pack()
        labelNombre.pack()
        entryNombre.pack()
        labelEdad.pack()
        entryEdad.pack()
        labelCarrera.pack()
        entryCarrera.pack()
        labelPromedio.pack()
        entryPromedio.pack()
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
                entryEdad.delete(0, tk.END)
                entryEdad.insert(0, str(valores[2]))
                entryCarrera.delete(0, tk.END)
                entryCarrera.insert(0, str(valores[3]))
                entryPromedio.delete(0, tk.END)
                entryPromedio.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventanaPrincipal.mainloop()