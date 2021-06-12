################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
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
            var2 = var1 + 32
        intermedio.append(chr(var2))
    return intermedio 



def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se ingresa una palabra en mayúsculas y
minúsculas y la función retorna la inversión entre ellas.
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            texto = str(input("Ingrese palabra: "))
            conversion = inversion(texto)
            print(f'La inversión queda: {conversion}')            
            sleep(10)
        elif test == 2:
            break       



if __name__ == "__main__":
    prueba()

