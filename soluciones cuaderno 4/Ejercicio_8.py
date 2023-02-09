
def iguales(cadena1, cadena2):
    """ str, str -> bool
    OBJ: Determina si dos cadenas son iguales """
    son_iguales = True
    if len(cadena1) != len(cadena2):
        son_iguales = False
    else:
        pos = 0
        while son_iguales and pos < len(cadena1):
            if cadena1[pos] != cadena2[pos]:
                son_iguales = False
            pos += 1
    return son_iguales

print(iguales('hola', 'hola'))