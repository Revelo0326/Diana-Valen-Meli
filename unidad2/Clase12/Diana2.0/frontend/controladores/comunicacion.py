import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/estudiante/'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, nombre, edad, carrera, promedio):
        try:
            print(nombre, edad, carrera, promedio)
            data = {
                'nombre': nombre,
                'edad': int(edad),
                'carrera': carrera,
                'promedio': float(promedio)
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json())
            return resultado
        except:
            pass

    def actualizar(self, id, nombre, edad, carrera, promedio):
        try:
            print(nombre, edad, carrera, promedio)
            data = {
                'nombre': nombre,
                'edad': int(edad),
                'carrera': carrera,
                'promedio': float(promedio)
            }
            resultado = requests.put(self.url + str(id)+ '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        try:
            resultado = requests.get(self.url + str(id))
            if resultado.status_code == 200:
                return resultado.json()
            else:
                return None
        except Exception as e:
            print(f"Error en consulta por ID: {e}")
            return None

    
    def consultar_todo(self, nombre, edad, carrera, promedio):
        url = self.url + "?"

        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&"
        if edad != '':
            url = url + 'edad=' + str(edad) + "&"
        if carrera != '':
            url = url + 'carrera=' + str(carrera) + "&"
        if promedio != '':
            url = url + 'promedio=' + str(promedio) + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()

    
    def eliminar(self, id):
        resultado = requests.delete(self.url + str(id))
        return resultado.status_code