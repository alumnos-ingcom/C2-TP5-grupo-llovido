################
# Agostina Biagini - @AgostinaB
# Ejercicio N°11: Palíndromo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    """Esta función recibe una palabra e indica "True" si es palíndromo
    (se lee igual de derecha a izquierda que de izquierda a derecha).
    """
    letras=[]
    letras_reversa=[]
    for i in range(len(texto)):
        letras.append(texto[i])
    
    for j in reversed(range(len(texto))):         
        letras_reversa.append(texto[j])
            
    if letras == letras_reversa:
        return True
    else:
        return False
    
    
def prueba():
    print('Ejercicio 11: Palíndromo \n')
    palabra = str (input("Ingrese palabra: "))
    resultado = es_palindromo(palabra)
    print(f'\n El resultado de evaluar {palabra} como palíndormo es: {resultado}')
        

if __name__ == "__main__":
    prueba() 