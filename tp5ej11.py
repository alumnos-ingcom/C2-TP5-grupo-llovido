################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 11 - Promedio movil
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



class ErrorN(Exception):
    '''En el caso de que n sea mayor que la longitud de la lista ingresada'''
    pass



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def promedio_movil(lista, n):
    '''
    Funcion que implemente aun promedio movil a una lista de numeros

    Un promedio móvil es una media no ponderada de una cantidad menor
    al total de un conjunto de valores en una serie de datos. Es una
    forma de controlar variaciones fuertes en la misma. Esta técnica
    permite ajustar el nivel de suavizado cambiando la cantidad de
    valores contiguos de la serie que entran en el calculo.
    
    Teoria: 
    https://school.stockcharts.com/doku.php?id=technical_indicators:moving_averages

    Argumento:
        lista(list):    Lista de numeros a ser promediada
        n(int):         Cantidad de posiciones

    Retorna:
        ret(list):      Lista promediada
    '''
    if n > len(lista):
        raise ErrorN("Se está queriendo promediar con un numero más grande que el largo de la lista")

    ret = []
    for i in range(0, len(lista) - n):
        l2 = []
        for j in range(n):
            l2.append(lista[i+j])
        
        promedio = 0
        for j in l2:
            promedio += j
        promedio = promedio / n
        
        ret.append(promedio)
        
        l2.clear()
    
    return ret



def prueba():
    """Toda la interacción con el usuario va acá"""
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(promedio_movil(l, 3))

if __name__ == "__main__":
    prueba()

