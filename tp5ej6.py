################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



def balanceo(texto, tipo='p'):
    '''
    Funcion que verifica que todo parentesis que se abra, sea cerrado.

    La funcion verificara que todos los parentesis que se abran en
    una cadena de caracteres de un determinado texto sean cerrados

    Valores ASCII:
        (:40
        ):41
        [:91
        ]:93
        {:123
        }:125

    Argumentos:
        texto(str): Texto a ser verificado
        tipo(str):  Tipo de signo:
                        p: parentesis
                        c: corchete
                        l: llave

    Retorna:
        ret(bool):      True en el caso de que todos los parentesis
                        esten completos. False en el caso contrario
    Ejemplos:
       (vacio)      OK
       []           OK   
       [][]         OK   
       [[][]]       OK 
       ][           NO OK
       ][][         NO OK
       []][[]       NO OK
    '''

    if (tipo == 'p'):
        abrir = 40
        cerrar = 41
    elif (tipo == 'c'):
        abrir = 91
        cerrar = 93
    elif (tipo == 'l'):
        abrir = 123
        cerrar = 125
    else:
        raise ValueError("tipo de signo invalido")
    contador = 0

    for i in range(len(texto)):
        if(contador == 0 and ord(texto[i]) == cerrar):
            contador -= 1
            break
        elif(ord(texto[i]) == abrir):
            contador += 1 
        elif(ord(texto[i]) == cerrar):
            contador -= 1
     
    if contador == 0:
        ret = True
    else:
        ret = False

    return ret



def prueba():
    """Toda la interacción con el usuario va aca"""
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se le tiene que ingresar un texto con 
parentesis o corchetes o llaves y la funcion indoca con
True si los signos estan balanceados y False en caso
contrario.
    Ingrese 1 para ingresar el texto de prueba
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            text = input("ingrese el texto >>> ")
            cosa = input("ingrese 'c' (corchete), 'l' (llave) o 'p' (parentesis) >>> ")
            resultado = balanceo(text, cosa)
            print(f'El numero es: {resultado}')
            sleep(60)
        elif test == 2:
            break



if __name__ == "__main__":
    prueba()

