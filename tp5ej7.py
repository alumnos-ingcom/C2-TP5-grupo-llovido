################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



def distancia(numero1, numero2):
    '''
    Funcion que devuelve la distancia entre 2 numeros.

    Argumentos:
        numero1(float), numero2(float): numeros cuya distancia
                                        debe ser medida
    Retorna:
        ret(float): distancia entre los argumentos
    '''
    resta = numero1 - numero2    
    if resta >= 0:
        return resta
    elif resta < 0:
        resta = resta*(-1)
        return resta
 
 
        
def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se ingresan dos números
y la funcion retorna la distancia entre ellos.
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            num1 = float(input(("ingrese un numero: ")))
            num2 = float(input(("ingrese otro numero: ")))
            resultado = distancia(num1, num2)
            print(f'La distancia entre {num1} y {num2} es: {resultado}')
            sleep(10)
        elif test == 2:
            break    



if __name__ == "__main__":
    prueba()

