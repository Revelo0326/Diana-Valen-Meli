import re

class Validaciones():
    
    def __init__(self):
        pass

    def validarLetras(valor):
        patron = re.compile("^[A-Za-zñÑ ]*$")
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True
    
    def validar_numeros(valor):
        patron = re.compile("^[0-9.,]*$")
        return patron.match(valor.get()) is not None

    def validar_alfanumerico(texto):
        return re.fullmatch(r'[A-Za-z0-9]*', texto) is not None