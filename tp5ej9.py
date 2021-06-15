################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 9 - Factoriones
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')    



def factorial(a):
    '''
    Funcion que devuelve el valor factorial de un número.

    Retorna:
        ret(factor) = factorial de número.
    '''    
     
    factor = 1
    for i in range(1,a+1):
        factor = factor*i
    
    return factor


    
def factorion():
    '''
    Funcion que devuelve una lista con todos los factoriones menor a 1.499.999.

    Un factorion es un numero natural cuya suma de los factoriales de los digitos
    que lo conforman es igual al mismo numero

    Retorna:
        ret(list) = lista con todos los factoriones hasta 1.499.999
    '''
    
    a = 200
    lista = []
    factoriones = []
    num = []
    for i in range (1, a):
        term = factorial(i)
        lista.append(term)
       
    res = []
    for millon in range(2):
        for cienmil in range(10):
            for diezmil in range(10):
                for mil in range(10):
                    for centena in range(10):
                        for decena in range(10):
                            for unidad in range(10):
                                num = millon*1000000 + cienmil*100000 + diezmil*10000 + mil*1000 + centena*100 + decena*10 + unidad
                                print(num)
                                variable = factorial(millon) + factorial(cienmil) + factorial(diezmil) + factorial(mil) + factorial(centena) + factorial(decena) + factorial(unidad)
                                if num == variable:
                                    res.append(num)
                                if num == 1500000:
                                    break
    return res 
        
   
                             
def prueba():
    """Toda la interacción con el usuario va acá"""
    limpiar_consola()
    resultado = factorion()
    print(f'La lista de factoriones es: {resultado}')
             
     
             
if __name__ == "__main__":
    prueba()

