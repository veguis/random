# Implementar una función que pone en mayúsculas la primera letra de cada una 
# de las palabras de una frase, sin usar el método title().

def mayusculas(frase):
    """ str --> str
        OBJ: pone en mayuscula la primera letra de cada palabra.
    """
    palabras = frase.split()
    frase_nueva=''
    for palabra in palabras:
        frase_nueva+=palabra[0].upper()
        for i in range(1,len(palabra)):
            frase_nueva+=palabra[i]
        frase_nueva+=' '
    return frase_nueva


#Probador
print(mayusculas('hola que tal'))
