import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
import time

URL_API = "http://127.0.0.1:8000/api"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Autores y Libros")
        self.root.geometry("900x600")
        self.root.configure(bg="#f2f2f2")

        self.pestañas = ttk.Notebook(self.root)
        self.pestañas.pack(fill='both', expand=True, padx=10, pady=10)

        self.frame_autores = ttk.Frame(self.pestañas)
        self.frame_libros = ttk.Frame(self.pestañas)

        self.pestañas.add(self.frame_autores, text="Autores")
        self.pestañas.add(self.frame_libros, text="Libros")

        self.construir_pestaña_autores()
        self.construir_pestaña_libros()

        self.ejecutar_respaldo = True
        threading.Thread(target=self.respaldo_automatico, daemon=True).start()

    # -------------------------- AUTORES --------------------------
    def construir_pestaña_autores(self):
        grupo = ttk.LabelFrame(self.frame_autores, text="Datos del Autor")
        grupo.pack(fill='x', padx=10, pady=10)

        ttk.Label(grupo, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.id_autor = ttk.Entry(grupo, width=30)
        self.id_autor.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(grupo, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.nombre_autor = ttk.Entry(grupo, width=30)
        self.nombre_autor.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(grupo, text="Nacionalidad:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.nacionalidad_autor = ttk.Entry(grupo, width=30)
        self.nacionalidad_autor.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(grupo, text="Edad:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.edad_autor = ttk.Entry(grupo, width=30)
        self.edad_autor.grid(row=3, column=1, padx=5, pady=5)


        acciones = ttk.Frame(self.frame_autores)
        acciones.pack(pady=10)
        for i, (texto, comando) in enumerate([
            ("Crear", self.crear_autor),
            ("Consultar Todos", self.consultar_lista_autores),
            ("Consultar por ID", self.consultar_autor_por_id),
            ("Actualizar", self.actualizar_autor),
            ("Borrar", self.borrar_autor),
            ("Limpiar", self.limpiar_formulario_autor)
        ]):
            ttk.Button(acciones, text=texto, command=comando).grid(row=0, column=i, padx=5)

        self.tabla_autores = ttk.Treeview(self.frame_autores, columns=("id", "nombre", "edad", "nacionalidad"), show="headings")
        for col in ("ID", "Nombre", "Edad", "Nacionalidad"):
            self.tabla_autores.heading(col.lower(), text=col)
            self.tabla_autores.column(col.lower(), width=100)
        self.tabla_autores.pack(fill='both', expand=True, padx=10, pady=10)

    def crear_autor(self):
        datos = {
            "nombre": self.nombre_autor.get(),
            "edad": self.edad_autor.get(),
            "nacionalidad": self.nacionalidad_autor.get()
        }
        response = requests.post(f"{URL_API}/autores/", json=datos)
        if response.status_code == 201:
            messagebox.showinfo("Éxito", "Autor creado correctamente")
            self.limpiar_formulario_autor()
        else:
            messagebox.showerror("Error", response.text)

    def consultar_lista_autores(self):
        response = requests.get(f"{URL_API}/autores/")
        if response.status_code == 200:
            self.tabla_autores.delete(*self.tabla_autores.get_children())
            for autor in response.json():
                self.tabla_autores.insert('', 'end', values=(autor['id'], autor['nombre'], autor['edad'], autor['nacionalidad']))
        else:
            messagebox.showerror("Error", response.text)

    def consultar_autor_por_id(self):
        id_ = self.id_autor.get()
        if not id_:
            return messagebox.showwarning("Advertencia", "Ingrese un ID")
        response = requests.get(f"{URL_API}/autores/{id_}/")
        if response.status_code == 200:
            autor = response.json()
            self.nombre_autor.delete(0, tk.END)
            self.nombre_autor.insert(0, autor['nombre'])
            self.edad_autor.delete(0, tk.END)
            self.edad_autor.insert(0, autor['edad'])
            self.nacionalidad_autor.delete(0, tk.END)
            self.nacionalidad_autor.insert(0, autor['nacionalidad'])
        else:
            messagebox.showerror("Error", response.text)

    def actualizar_autor(self):
        id_ = self.id_autor.get()
        if not id_:
            return messagebox.showwarning("Advertencia", "Ingrese un ID")
        datos = {
            "nombre": self.nombre_autor.get(),
            "edad": self.edad_autor.get(),
            "nacionalidad": self.nacionalidad_autor.get()
        }
        response = requests.put(f"{URL_API}/autores/{id_}/", json=datos)
        if response.status_code in (200, 204):
            messagebox.showinfo("Éxito", "Autor actualizado correctamente")
            self.limpiar_formulario_autor()
        else:
            messagebox.showerror("Error", response.text)

    def borrar_autor(self):
        id_ = self.id_autor.get()
        if not id_:
            return messagebox.showwarning("Advertencia", "Ingrese un ID")
        response = requests.delete(f"{URL_API}/autores/{id_}/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Autor borrado correctamente")
            self.limpiar_formulario_autor()
        else:
            messagebox.showerror("Error", response.text)

    def limpiar_formulario_autor(self):
        self.id_autor.delete(0, tk.END)
        self.nombre_autor.delete(0, tk.END)
        self.edad_autor.delete(0, tk.END)
        self.nacionalidad_autor.delete(0, tk.END)

    # -------------------------- LIBROS --------------------------
    def construir_pestaña_libros(self):
        grupo = ttk.LabelFrame(self.frame_libros, text="Datos del Libro")
        grupo.pack(fill='x', padx=10, pady=10)

        ttk.Label(grupo, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.id_libro = ttk.Entry(grupo, width=30)
        self.id_libro.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(grupo, text="Título:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.titulo_libro = ttk.Entry(grupo, width=30)
        self.titulo_libro.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(grupo, text="Género:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.genero_libro = ttk.Entry(grupo, width=30)
        self.genero_libro.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(grupo, text="Páginas:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.paginas_libro = ttk.Entry(grupo, width=30)
        self.paginas_libro.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(grupo, text="Año Publicación:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.anio_libro = ttk.Entry(grupo, width=30)
        self.anio_libro.grid(row=4, column=1, padx=5, pady=5)

        acciones = ttk.Frame(self.frame_libros)
        acciones.pack(pady=10)
        for i, (texto, comando) in enumerate([
            ("Crear", self.crear_libro),
            ("Consultar Todos", self.consultar_lista_libros),
            ("Consultar por ID", self.consultar_libro_por_id),
            ("Actualizar", self.actualizar_libro),
            ("Borrar", self.borrar_libro),
            ("Limpiar", self.limpiar_formulario_libro)
        ]):
            ttk.Button(acciones, text=texto, command=comando).grid(row=0, column=i, padx=5)

        self.tabla_libros = ttk.Treeview(self.frame_libros, columns=("id", "titulo", "genero", "paginas", "anio"), show="headings")
        for col in [("id", "ID"), ("titulo", "Título"), ("genero", "Género"), ("paginas", "Páginas"), ("anio", "Año")]:
            self.tabla_libros.heading(col[0], text=col[1])
            self.tabla_libros.column(col[0], width=100)
        self.tabla_libros.pack(fill='both', expand=True, padx=10, pady=10)

    def crear_libro(self):
        datos = {
            "titulo": self.titulo_libro.get(),
            "genero": self.genero_libro.get(),
            "paginas": self.paginas_libro.get(),
            "año_publicacion": self.anio_libro.get()
        }
        response = requests.post(f"{URL_API}/libros/", json=datos)
        if response.status_code == 201:
            messagebox.showinfo("Éxito", "Libro creado correctamente")
            self.limpiar_formulario_libro()
        else:
            messagebox.showerror("Error", response.text)

    def consultar_lista_libros(self):
        response = requests.get(f"{URL_API}/libros/")
        if response.status_code == 200:
            self.tabla_libros.delete(*self.tabla_libros.get_children())
            for libro in response.json():
                self.tabla_libros.insert('', 'end', values=(
                    libro['id'], libro['titulo'], libro['genero'],
                    libro['paginas'], libro['año_publicacion']
                ))
        else:
            messagebox.showerror("Error", response.text)

    def consultar_libro_por_id(self):
        id_ = self.id_libro.get()
        if not id_:
            return messagebox.showwarning("Advertencia", "Ingrese un ID")
        response = requests.get(f"{URL_API}/libros/{id_}/")
        if response.status_code == 200:
            libro = response.json()
            self.titulo_libro.delete(0, tk.END)
            self.titulo_libro.insert(0, libro['titulo'])
            self.genero_libro.delete(0, tk.END)
            self.genero_libro.insert(0, libro['genero'])
            self.paginas_libro.delete(0, tk.END)
            self.paginas_libro.insert(0, libro['paginas'])
            self.anio_libro.delete(0, tk.END)
            self.anio_libro.insert(0, libro['año_publicacion'])
        else:
            messagebox.showerror("Error", response.text)

    def actualizar_libro(self):
        id_ = self.id_libro.get()
        if not id_:
            return messagebox.showwarning("Advertencia", "Ingrese un ID")
        datos = {
            "titulo": self.titulo_libro.get(),
            "genero": self.genero_libro.get(),
            "paginas": self.paginas_libro.get(),
            "año_publicacion": self.anio_libro.get()
        }
        response = requests.put(f"{URL_API}/libros/{id_}/", json=datos)
        if response.status_code in (200, 204):
            messagebox.showinfo("Éxito", "Libro actualizado correctamente")
            self.limpiar_formulario_libro()
        else:
            messagebox.showerror("Error", response.text)

    def borrar_libro(self):
        id_ = self.id_libro.get()
        if not id_:
            return messagebox.showwarning("Advertencia", "Ingrese un ID")
        response = requests.delete(f"{URL_API}/libros/{id_}/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Libro borrado correctamente")
            self.limpiar_formulario_libro()
        else:
            messagebox.showerror("Error", response.text)

    def limpiar_formulario_libro(self):
        self.id_libro.delete(0, tk.END)
        self.titulo_libro.delete(0, tk.END)
        self.genero_libro.delete(0, tk.END)
        self.paginas_libro.delete(0, tk.END)
        self.anio_libro.delete(0, tk.END)

    # -------------------------- RESPALDO AUTOMÁTICO --------------------------
    def respaldo_automatico(self):
        while getattr(self, "ejecutar_respaldo", True):
            try:
                autores = requests.get(f"{URL_API}/autores/").json()
                libros = requests.get(f"{URL_API}/libros/").json()

                with open("respaldo_autores.txt", "w", encoding="utf-8") as fa:
                    for a in autores:
                        fa.write(f"Nombre: {a['nombre']}\nNacionalidad: {a['nacionalidad']}\nEdad: {a['edad']}\n\n")

                with open("respaldo_libros.txt", "w", encoding="utf-8") as fl:
                    for l in libros:
                        fl.write(f"Título: {l['titulo']}\nGénero: {l['genero']}\nPáginas: {l['paginas']}\nAño: {l['año_publicacion']}\n\n")
            except Exception as e:
                print("[Error en respaldo]:", e)
            time.sleep(60)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    def al_cerrar():
        app.ejecutar_respaldo = False
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", al_cerrar)
    root.mainloop()
