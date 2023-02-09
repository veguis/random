lista1=[1, 2, 3, 4, 5]
lista2=[8, 6, 5, 9, 10]

def suma(lista1, lista2):
    """ list, list -> list
        OBJ: crea una lista con el resultado de la suma de los elemento de otras dos listas.
        PRE: listas numéricas.
    """
    listasuma=[]
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        listasuma.append(suma)
    return listasuma

print(suma(lista1, lista2))