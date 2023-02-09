# Una lista de enteros original debe utilizarse para generar dos listas, una con los 
# números pares de la original ordenados ascendentemente y otra con los impares 
# ordenados  descendentemente.  La  generación  de  las  2  listas  debe  hacerse  a 
# medida que se recorre la original, es decir, se toma un número de la original, se 
# decide a qué lista (pares o impares) debe ir, y se inserta ordenado en la misma 
# de acuerdo con el criterio de la lista (ascendente o descendente).

#NO ESTA BIEN HECHO, MIRAR SOLUCIONES!!!

import random

def ordenar_listas(lista):
    """ list --> list, list
        OBJ: a partir de una lista se crean dos listas ordenadas una de numeros pares y otra de impares.
    """
    pares = []
    impares = []
    ini_par = 0
    ini_impar = 0
    for i in range(len(lista)):
        fin_par = len(pares)
        fin_impar = len(impares)

        if lista[i] % 2 == 0:
            pos = pos_orden_ascendente(lista[i], pares)
            pares.insert(pos, lista[i])
        else:
            impares.append(lista[i])
    
    print(pares)
    print(impares)

def pos_orden_ascendente(num ,lista):
    """ int, list --> list
        OBJ: inserta un elemento en una lista de forma ascendente.
    """
    ini = 0
    fin = len(lista)
    while ini <= fin:
        if lista == []:
            lista.append(num)
        else:
            for item in lista:
                if item < num:
                    i = lista.index(item)
                else:
                    i = lista.index(item) + 1
        ini += 1
        fin -= 1
    return i

lista = []
for i in range(20):
    lista.append(random.randint(0,100))
print(lista)
ordenar_listas(lista)
