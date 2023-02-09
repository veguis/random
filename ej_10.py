# Escriba un programa que “codifique” una frase modificando todas las vocales 
# según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el símbolo #. 
# Por ejemplo, la frase: “Un perro del hortelano”, deberá devolverse: “#n p3rr0 d3l 
# h0rt3l4n0”.

def modificar_frase(cadena):
    """ str --> str
        OBJ: modifica las vocales de un frase cambiando: a por 4, e por 3, i por 1, o por 0 y u por el símbolo #.
    """
    VOCALES = [('a', 'á', 'A'),('e', 'é', 'E'),('i', 'í', 'I'),('o', 'ó', 'O'),('u', 'ú', 'U')]
    frase_nueva = ''
    for item in cadena:
        if item in VOCALES[0]:
            frase_nueva += '4'
        elif item in VOCALES[1]:
            frase_nueva += '3'
        elif item in VOCALES[2]:
            frase_nueva += '1'
        elif item in VOCALES[3]:
            frase_nueva += '0'
        elif item in VOCALES[4]:
            frase_nueva += '#'
        else:
            frase_nueva += item
    return frase_nueva

print(modificar_frase('Un perro del hortelano.'))
