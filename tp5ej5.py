################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1.py as inp
from time import sleep



def inversion(texto):
    '''
    Función que invierte la letra de un texto.

    Ejemplo:
        Si ingresa 'Hola Mundo!', la salida de la funcion debe
        ser: 'hOLA mUNDO!'

    Argumentos:
        texto(string):  cadena de caracteres a invertir

    Retorna:
        txt(string):    cadena de caracteres invertida
    '''
    intermedio = []

    for i in range(len(texto)):
        var1 =  ord(texto[i])
        if (var1 >= 97 and var1 <= 122):
            var2 = var1 - 32
        elif (var1 >= 65 and var1 <= 90):
            var2 = i + 32
        intermedio.append(var2)

def prueba():
    """Toda la interacción con el usuario va acá"""
    pass

if __name__ == "__main__":
    prueba()

