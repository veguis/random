def peso(lista):
    """ list -> float
        OBJ: calcula los pesos de la un lista sumando los abs de sus valores.
        PRE: lista numerica.
    """
    peso = 0
    for item in lista:
        peso += abs(item)
    return peso


def max_peso(peso1, peso2):
    """ float, float -> float
        OBJ: compara los pesos de dos listas y retorna el mayor.
        PRE: listas numéricas.
    """
    return max(peso1,peso2)
    
#Probador
lista1=[1, 2, 3, 5, 6, 8]
lista2=[2, 3, 54, -87, 5]
print(peso(lista1), ',', peso(lista2), ',', max_peso(peso(lista1),peso(lista2)))
