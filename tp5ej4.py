################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



def numeros_perfectos(numero):
    '''
    Funcion que determina si un numero es o no perfecto.

    argumentos:
        numero(int):    numero a ser probado

    retorna:
        ret(bool):      Retorna True si el numero es perfecto
                        y False en caso contrario
    '''
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i
    if numero == suma:
        return True
    else:
        return False
        
        
        
def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se le tiene que ingresar un numero
y la funcion retorna True si el numero es perfecto y 
False si el numero no lo es.
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            n = inp.ingreso_entero("ingrese numero")
            resu = numeros_perfectos(n)
            print(f'La evaluación de {n} como perfecto resultó: {resu}')
            sleep(10)
        elif test == 2:
            break
        
        
        
if __name__ == "__main__":
    prueba()

