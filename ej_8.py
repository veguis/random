# Crear una función que compruebe si dos cadenas de caracteres son iguales, sin 
# comparar las cadenas completas y sin usar el operador in.

def son_iguales(cadena1, cadena2):
    """ str, str --> bool
        OBJ: comprueba si dos cadenas de caracteres son iguales
    """
    inicio = 0
    fin = min(len(cadena1),len(cadena2))
    iguales = True
    while iguales and inicio <= fin:
        for i in range(inicio, fin+1):
            if cadena1[i] != cadena2[i]:
                iguales = False
            else:
                inicio += 1
    return iguales


#Probador
palabra1 = 'hola'
palabra2 = 'hola'
print(son_iguales(palabra1, palabra2))
