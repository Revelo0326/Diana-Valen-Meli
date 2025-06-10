 📚 Sistema de Gestión de Libros

Este proyecto está desarrollado en Python y tiene como objetivo principal la gestión integral de libros, autores y editoriales. La estructura del sistema sigue una arquitectura modular bien definida, separando claramente la lógica del backend y la interfaz del frontend para facilitar el mantenimiento, la escalabilidad y la colaboración entre desarrolladores.

El backend se encarga de la lógica del negocio, el manejo de datos y la comunicación con la base de datos, mientras que el frontend proporciona una interfaz amigable para que los usuarios interactúen con el sistema. Como motor de base de datos se utiliza SQLite, una solución liviana y eficiente que permite un almacenamiento local de datos sin necesidad de un servidor adicional, ideal para aplicaciones de escritorio o prototipos funcionales.


## 🧾 Descripción General

El sistema permite:

- Registrar, modificar y eliminar autores.
- Gestionar libros, incluyendo relaciones con autores.
- Mostrar información desde un frontend modular.

## 📁 Estructura del Proyecto

```
Proyecto final/
├── backend/
│   ├── app/
│   ├── autor/
│   ├── libro/
│   ├── db.sqlite3
│   └── manage.py
├── frontend/
│   └── main.py
├── README.md
├── respaldo_autores.txt
└── respaldo_libros.txt
```

## ⚙️ Requisitos

Requiere Python 3.7 o superior.

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt
```

## 🚀 Ejecución

### 1. Ejecutar el Backend

Desde la raíz del proyecto:

```bash
cd backend
```

Si es la primera vez que ejecutas el proyecto o has realizado cambios en los modelos, ejecuta:

```bash
python manage.py makemigrations
python manage.py migrate
```

Luego, para iniciar el servidor:

```bash
python manage.py runserver
```

### 2. Ejecutar el Frontend

```bash
cd frontend
python main.py
```

## 💾 Base de Datos

- Se utiliza `SQLite` y se incluye el archivo `db.sqlite3`.
- Para restaurar datos puedes usar los archivos:
  - `respaldo_autores.txt`
  - `respaldo_libros.txt`

## 🧩 Módulos

- **Autor**: Control de información de autores.
- **App**: Gestión de editoriales.
- **Libro**: Registro de libros y sus relaciones.
- **Frontend**: Presentación de la información (posiblemente consola o interfaz gráfica básica).

## 📌 Notas Adicionales

- Estructura limpia y separada por capas (modelo, vista, controlador).
- Se recomienda hacer respaldos periódicos de `db.sqlite3`.





