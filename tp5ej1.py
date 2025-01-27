################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 1 - Pares e impares
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
import tp4ej7 as div
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def es_par(numero):
    """
    Función que indica si el número es par o impar.

    atributos:
        numero(int): numero a ser probado

    retorna:
        True: si el numero es par
        False: si el numero es impar
    """
    cociente, resto = div.division_lenta(numero, 2)
    if resto == 0:
        return True
    else:
        return False



def prueba():
    """Toda la interacción con el usuario va aca"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se le tiene que ingresar un numero
y la funcion retorna True si el numero es par y 
False si el numero es impar
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            n = inp.ingreso_entero("ingrese numero de prueba")
            resultado = es_par(n)
            print(f'El numero es: {resultado}')
            sleep(10)
        elif test == 2:
            break



if __name__ == "__main__":
    prueba()
