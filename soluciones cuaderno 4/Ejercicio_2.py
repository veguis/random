
def sumar_listas(lista1, lista2):
    """ list, list --> list
    OBJ: Devuelve una lista con la suma de las dos
    """
    if len(lista1) <= len(lista2):
        menor = lista1
        mayor = lista2
    else:
        menor = lista2
        mayor = lista1
    resul = []
    for i in range(len(menor)):
        resul += [menor[i] + mayor[i]]
    for i in range(len(menor),len(mayor)):
        resul += [mayor[i]]
    return resul

print(sumar_listas([1,2,3,4],[2,2,2,2,2,2]))
print(sumar_listas([1,2,3,4,5,6],[2,2,2,2]))