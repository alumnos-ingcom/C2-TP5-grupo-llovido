################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 11 - Promedio movil
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep
from generador_listas import lista_random



class ErrorLongitudesDiferntes(Exception):
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
        raise ErrorLongitudesDiferntes("Se está queriendo promediar con un numero más grande que el largo de la lista")

    ret = []
    for i in range(0, len(lista) - n + 1):
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
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresa una lista de numeros
y un numero para ir moviendose. La funcion tiene que
retornar el promedio movil de la lista en base al
numero movil
    Ingrese 1 para ingresar lista definida por el usuario y numero movil
    Ingrese 2 para ingresar lista aleatoria pero numero movil definido por usuario
    Ingrese 3 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 3)
        if test == 1:
            movil = inp.ingreso_entero("Ingrese el valor del n")
            largo = inp.ingreso_entero("ingrese el largo de la lista")

            listita = []
            for i in range(largo):
                aux = inp.ingreso_entero(f"Ingrese el {i+1}esimo valor")
                listita.append(aux)
            print(f"La lista final es: {listita}")

            resultado = promedio_movil(listita, movil)
            print(f'''El promedio movil de la lista {listita} con movil {movil} es:
                    {resultado}''')
            sleep(10)
        elif test == 2:
            listita = lista_random()
            movil = inp.ingreso_entero("Ingrese el valor del n")
            print(f"La lista final es: {listita}")

            resultado = promedio_movil(listita, movil)
            print(f'''El promedio movil de la lista {listita} con movil {movil} es:
                    {resultado}''')
            sleep(10)
        elif test == 3:
            break    


if __name__ == "__main__":
    prueba()

