################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1.py as inp

def es_par(numero):
    """
    Función que indica si el número es par o impar.

    atributos:
        numero(int): numero a ser probado

    retorna:
        True: si el numero es par
        False: si el numero es impar
    """
    pass

def prueba():
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se le tiene que ingresar un numero
y la funcion retorna True si el numero es par y 
False si el numero es impar
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            sleep(10)
        elif test == 2:
            break

if __name__ == "__main__":
    prueba()

