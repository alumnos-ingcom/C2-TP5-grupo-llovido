################
# Agostina Biagini - @AgostinaB
# Ejercicio N°7: Restas sucesivas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def division_lenta (dividendo, divisor):
    """Esta función mediante restas sucesivas, obtiene el cociente y
    el resto de dos números enteros.
    """
    contador =0    
    if dividendo >= divisor :
        while dividendo >= divisor :
            dividendo = dividendo - divisor
            contador = contador + 1
        return contador, dividendo
 
def prueba():
    print('Ejercicio 7: Restas sucesivas \n')
    dividendo = int (input("Ingrese dividendo: "))
    divisor = int (input("Ingrese divisor: "))
    cociente, resto = division_lenta (dividendo, divisor)
    print(f'El cociente es : {cociente}, y el resto es: {resto}')
    
    
if __name__ == "__main__":
    prueba() 