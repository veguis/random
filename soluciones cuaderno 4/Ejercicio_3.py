import random

def inserta_ordenado_ascendente(lista, num):
    """ list, int -> list
    OBJ: Devuelve una lista con el número insertado en orden ascendente """
    res = []
    if len(lista) == 0:
        res += [num]
    else:
        pos = 0
        while pos < len(lista) and lista[pos] < num:
            pos += 1
        if pos == len(lista):
            res = lista + [num]
        else:
            res = lista[:pos] + [num] + lista[pos:]
    return res

lista = []
for i in range(10):
    lista += [random.randint(1,100)]
print(lista)

pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares = inserta_ordenado_ascendente(pares, num)
    else:
        impares = inserta_ordenado_ascendente(impares, num)
impares = impares[::-1]

print(pares)
print(impares)
