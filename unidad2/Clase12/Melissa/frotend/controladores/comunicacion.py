import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/api/usuario/'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, nombre, correo,telefono,pin):
        try:
            print(nombre, correo,telefono,pin)
            data = {
                'nombre': nombre,
                'correo': correo,
                'telefono': telefono,
                'pin': pin,
            }
            #resultado = requests.post(self.url, json=data)
            #print(resultado.json)
            return requests.post(self.url, json=data)
        except ValueError:
            return False

    def actualizar(self, id, nombre, correo, telefono,pin):
        try:
            print(nombre, correo, telefono, pin)
            data = {
                'nombre': nombre,
                'correo': correo,
                'telefono': telefono,
                'pin': pin
            }
            resultado = requests.put(self.url + str(id) + '/', json=data)
            print(resultado.json)
            return resultado
        except ValueError:
            return False
    
    def consultar(self, id):
        resultado = requests.get(self.url + str(id))
        return resultado.json()
    
    def consultar_todo(self, nombre, correo, telefono,pin):
        url = self.url + "?"
        print(type(pin))
        
        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&" 
        if correo != '':
            url = url + 'correo=' + str(correo) + "&"
        if telefono != '':
            url = url + 'telefono=' + str(telefono) + "&"
        if pin != '':
            url = url + 'pin=' + str(pin) + "&"
        
        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code