################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 5 - Inversion de mayusculas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



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
            var1 = var1 - 32
        elif (var1 >= 65 and var1 <= 90):
            var1 = var1 + 32
        intermedio.append(chr(var1))
    return "".join(intermedio) 



def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresa una palabra en mayúsculas y
minúsculas y la función retorna la inversión entre ellas.
    Ingrese 1 para ingresar texto a invertir
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

