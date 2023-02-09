def suma_matrices(matriz1, matriz2):
    """ list, list -> list
        OBJ: suma matrices de mxn.
        PRE: listas numericas y del mismo tamaño.
    """
    matriz_sol = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(matriz1[i][j]+matriz2[i][j])
        matriz_sol.append(fila)
    return matriz_sol

#Probador
matrizA = [[1, 1], [2, 7]]
matrizB = [[0, 7], [10, 20]]
print(suma_matrices(matrizA, matrizB))
