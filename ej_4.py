#Crear una lista de enteros, inicializarlos según valores aleatorios en el rango 1..20
#y computar la media de los valores, el valor más alto y el más bajo (todo ello
#utilizando listas).

import random

lista_random = []
for i in range (0, 20):
    lista_random.append(random.randint(1,20))
print(lista_random)

# media = suma / num_items
suma = 0
for item in lista_random:
    suma += item
print(suma)

num_items = len(lista_random)
print(num_items)

media = suma / num_items
print('La media es', media)
