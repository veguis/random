
def es_palindromo(cadena):
    """ str --> bool
    OBJ: Comprueba si la cadena es un palíndromo. """
    ini = 0
    fin = len(cadena) - 1
    palindromo = True
    while palindromo and ini < fin:
        if cadena[ini] != cadena[fin]:
            palindromo = False
        else:
            ini += 1
            fin -= 1
    return palindromo

# Programa principal
cadena = input('Introduce una cadena: ')
print(es_palindromo(cadena))
