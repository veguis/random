def matriz_traspueta(matriz):
    """ list -> list
        OBJ: calcula la traspuesta de la matriz.
        PRE: lista numérica.
    """
    matriz_traspuesta = []
    if matriz==[]: return []
    else:
        for i in range(len(matriz[0])):
            fila = []
            for j in range(len(matriz)):
                fila.append(matriz[j][i])
            matriz_traspuesta.append(fila)
        return matriz_traspuesta

matrizA = [[1, 0, 0], [7, 1, 4]]
print(matriz_traspueta(matrizA))
