def capitalizada(cad):
    palabras=cad.split()
    nueva=''
    for palabra in palabras:
        nueva+=palabra[0].upper()
        for i in range(1,len(palabra)):
            nueva+=palabra[i]
        nueva+=' '
    return (nueva)

cadena='Esto es una frase para una prueba'
print(capitalizada(cadena))



