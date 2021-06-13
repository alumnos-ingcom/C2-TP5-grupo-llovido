################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
import tp4ej7 as division
from time import sleep



def binario(numero):
    '''
    Función que recibe un número entero positivo y retorna una cadena de texto
    con su representación binaria.

    Argumentos:
        numero(int): numero entero positivo ingresado por el usuario.
    
    Retorna:
        ret(str): cadena de texto con la representación binaria del número.
    '''
    
    lista = []
    final = []
    valor = numero
    if numero>0:
        while (valor >= 2):
            valor, resto = division.division_lenta(valor, 2)
            lista.append(resto)
    else:
        raise ValueError("El número no es un entero positivo")  
      
    for i in reversed(range(len(lista))):
        final.append(str(lista[i]))            
   
    return "".join(final)


        
def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se ingresa un número
y la funcion retorna una cadena con su representación binaria.
    Ingrese 1 para ingresar número
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            numero = int(input(("ingrese un número entero positivo: ")))
            resultado = binario(numero)
            print(f'La representación binaria de {numero} es: {resultado}')
            sleep(10)
        elif test == 2:
            break    



if __name__ == "__main__":
    prueba()