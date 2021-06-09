################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def fibonacci(n, call=True):
    """
    Funcion que retorna el n-esimo termino de la sucesion de fibonacci.

    El valor ingresado debe ser un entero positivo mayor a 2.
    En el caso que se le ingrese 0 o 1, la funcion levanta un ValueError
    avisando de que el numero debe ser mayor a 2.
    En el caso que el numero ingresado sea negativo, la funcion levanta
    otro ValueError que avisa que el numero ingresado debe ser un 
    entero positivo mayor a 2

    Parametros:
        n(int): valor de la iteracion a retornar
        call(bool):     indicador de si es la primer llamada a la funcion
                        o si se trata de alguna recursión

    retorna:
        ret(int):       retorna el resultado del n-esimo termino de la
                        sucesion de fibonacci
    """
    if n < 0:
        raise ValueError("se tiene que ingresar un numero positivo mayor a 2")
    if n == 0 or n == 1:
        if call:
            raise ValueError("n tiene que ser mayor que 2")
        ret = 1
    else:
        ret = fibonacci(n - 1, call=False) + fibonacci(n - 2, call=False)
    return ret

def prueba():
    """Toda la interacción con el usuario va acá"""
    print(fibonacci(5))

if __name__ == "__main__":
    prueba()

