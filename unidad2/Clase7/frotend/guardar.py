import requests


def guardar():
    datos={ 
        "id": 3,
        "nombre": "Daniela",
        "correo": "Daniela.acero@correounivalle.edu.co",
        "telefono": "3175282369",
        "pin": "2356",
        "fecha_creacion": "2025-04-08T00:22:37.060407Z"
         }

    respuesta = requests.post("http://127.0.0.1:8000/api/usuario/", json=datos)
    if respuesta.status_code == 201:
        print("Datos guardados correctamente.")
    else:
        print("Error al guardar datos")
    
guardar()