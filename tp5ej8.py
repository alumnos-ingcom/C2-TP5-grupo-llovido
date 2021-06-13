################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################
'''
El cifrado César o cifrado de rotación usa una encriptación de sustitución
simple. Esto significa que cada caracter se sustituye por otro caracter
de acuerdo con un sistema especifico. 

La codificación debe ser tal que la palabra codificada contenga unicamente
caracteres del tipo A-Z a-z y 0 a 9, de manera que al codificar las ultimas
letras del abecedario se vuelva a las primeras letras.

**Por ejemplo**, el método conocido y muy utilizado ROT13 rota el alfabeto
con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.
'''


import tp4ej1 as inp
from time import sleep

def rotacion(letra, rotate, minimo, maximo):
    if letra >= minimo and letra <= maximo:
        letra += rotate
        if letra > maximo:
            if maximo == 57: #si es digito, tengo que volver menos
                letra -= 10
            else:            #si es letra, vuelvo mas
                letra -= 25
    return letra



def codificado_cesar(texto, rotate):
    '''
    Funcion que implementa el cifrado cesar a una cadena de caracteres.

    Argumentos:
        texto(str):     cadena de caracteres a ser codificada
        rotate(int):    cantidad de posiciones a rotar el caracter

    Retorna:
        ret(str):       cadena de caracteres codificada segun el valor
                        de rotate
    '''
    for i in range(len(texto)):
        valor = ord(texto[i])
        
        #mayusculas A = 65...Z = 90
        valor = rotacion(valor, rotate, 65, 90)

        #minusculas a = 97...z = 122
        valor = rotacion(valor, rotate, 97, 122)

        #digitos 0 = 48...9 = 57
        valor = rotacion(valor, rotate, 48, 57)
    



def decodificado_cesar(text, rotate)
    pass



def prueba():
    """Toda la interacción con el usuario va acá"""
    pass

if __name__ == "__main__":
    prueba()

