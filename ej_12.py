# Escribir una función que permita mostrar los caracteres de una cadena del final 
# al principio, pero nunca mostrando la letra “a”. Ejemplo: si la entrada es “barco 
# amarillo”, la función devolverá: “ollirm ocrb”.

def cambiar_cadena(frase):
    """ str --> str
        OBJ: muestra los caracteres de una cadena del final al principio, pero nunca mostrando la letra “a”.
    """
    resultado = ''
    for i in range(len(frase) - 1, -1, -1):
        if frase[i] == 'a':
            resultado = resultado
        else:
            resultado += frase[i]
    print(resultado)

cambiar_cadena('barco amarillo')