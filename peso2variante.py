def peso(lista):
    """ list -> float
        OBJ: calcula los pesos de la un lista sumando los abs de sus valores.
    """
    peso = 0
    for item in lista:
        if type(item) in (int, float):
            peso += abs(item)
        else: peso += 1
    return peso


def max_peso_listas(lista):
    """ list -> float
        OBJ: determina el peso de las sublistas de una lista y retorna el mayor
        PRE: lista de listas numéricas.
    """
    lista_pesos = []
    for sublista in lista:
        lista_pesos.append(peso(sublista))
    return max(lista_pesos)
