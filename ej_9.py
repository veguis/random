# Implemente una función que indique si una palabra contiene las cinco vocales: 
# por ejemplo “murciélago”. Modifique posteriormente la función para que detecte 
# sólo aquellas palabras que contienen una única vez cada vocal.

def contiene_vocales(palabra):
    """ str --> bool
        OBJ: determinar si una palabra tiene las cinco vocales
    """
    VOCALES = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
    estan = False
    i = 0
    for caracter in palabra:
        if caracter in VOCALES:
            i += 1
    if i >= 5:
        estan = True
    return estan

#print(contiene_vocales('Murciélago'))
#print(contiene_vocales('Murciélagoae'))
#print(contiene_vocales('Casa'))
#print(contiene_vocales('Aaaaaae'))


def contiene_vocales2(palabra):
    """ str --> bool
        OBJ: determinar si una palabra tiene las cinco vocales
    """
    VOCALES = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
    estan = True
    vocales = []
    for caracter in palabra:
        if caracter in VOCALES:
            vocales.append(caracter)
    
    for elemento in vocales:
        #print(vocales.count(elemento))
        if vocales.count(elemento) > 1:
            estan = False

    #print(vocales)
    return estan


print(contiene_vocales2('Murciélago'))
print(contiene_vocales2('Murciélagoae'))
print(contiene_vocales2('Casa'))
print(contiene_vocales2('Aaaaaae'))
