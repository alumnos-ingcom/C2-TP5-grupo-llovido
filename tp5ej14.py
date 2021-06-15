################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 14 - Numeros capicua
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
import tp4ej11 as palindromo
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def capicua(numero):
    '''
    Función que indica si un número entero positivo es capicúa.

    Argumentos:
        numero(int): numero ingresado por el usuario.
    
    Retorna:
        ret(bool): True si el número es capicúa o False si no lo es.
    '''
    
    if numero > 0:
        texto = str(numero)
        if palindromo.es_palindromo(texto):
            ret = True
        else:
            ret = False
    else:
        raise ValueError("El número no es positivo")
    return ret    
 
 
        
def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresan dos números
y la funcion retorna la distancia entre ellos.
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            numero = int(input(("ingrese un número entero positivo: ")))
            resultado = capicua(numero)
            print(f'La evaluación resultó: {resultado}')
            sleep(3)
        elif test == 2:
            break    



if __name__ == "__main__":
    prueba()
