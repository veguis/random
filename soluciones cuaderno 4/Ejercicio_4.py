import random

NUM_ELEMENTOS = 10

lista_enteros = []
for i in range(NUM_ELEMENTOS):
    lista_enteros += [random.randint(1, 20)]

suma = 0
minimo = lista_enteros[0]
maximo = lista_enteros[0]
for num in lista_enteros:
    suma += num
    if num < minimo:
        minimo = num
    if num > maximo:
        maximo = num
media = suma / len(lista_enteros)

print(f"Lista generada: {lista_enteros}")
print(f"Media: {media}, minimo: {minimo}, maximo: {maximo}")
