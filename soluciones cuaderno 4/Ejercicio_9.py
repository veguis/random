
def tiene_5_vocales(cadena):
    """str --> bool
    OBJ: Comprueba si una cadena tiene las 5 vocales.
    """
    VOCALES = (('a', 'á'), ('e', 'é'), ('i', 'í'), ('o', 'ó'), ('u', 'ú'))
    cuenta_vocales = [0] * len(VOCALES)
    for caracter in cadena:
        i = 0
        encontrado = False
        while i < len(VOCALES) and not encontrado:
            if caracter.lower() in VOCALES[i]:
                cuenta_vocales[i] += 1
                encontrado = True
            i += 1
    resultado = True
    pos = 0
    while resultado and pos < len(cuenta_vocales):
        if cuenta_vocales[pos] != 1:
            resultado = False
        pos += 1
    return resultado

print(tiene_5_vocales('murciélago'))
print(tiene_5_vocales('murciélagoa'))
print(tiene_5_vocales('patata'))
