################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IteracionDebajoRango(Exception):
    """
    Excepcion en el caso de que el numero ingresado sea menor o igual a 2
    """
    pass

def fibonacci(iteracion): 
    if iteracion == 0 or iteracion == 1:
        ret = 1
    else:
        ret = fibonacci(n - 1) + fibonacci(n -2)
    return ret

def prueba():
    """Toda la interacción con el usuario va acá"""
    pass

if __name__ == "__main__":
    prueba()

