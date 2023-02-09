# Implementar  una  función  que  compruebe  si  una  palabra  es  un  palíndromo. 
# Atención, no hagas más trabajo del necesario. 

def es_palindromo(palabra):
    """ str -> bool
        OBJ: determina si una palabra es un palíndromo
    """
    inicio = 0
    fin = len(palabra) - 1
    palindromo = True
    while palindromo and inicio <= fin:
        if palabra[inicio] != palabra[fin]:
            palindromo = False
        else:
            inicio += 1
            fin -= 1
    return palindromo


#Probador
palabra = 'aopoa'
print(es_palindromo(palabra))