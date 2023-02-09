# Modificar una lista de números reales que representan las calificaciones de los
# alumnos de una clase, para sustituir los valores numéricos por sus calificaciones
# alfanuméricas (Suspenso, Aprobado, etc.)

import random

lista_notas = []
lista_calificaciones_alfanumericas = []

for i in range(9):
    lista_notas.append(random.randint(0,10))

print(lista_notas)

for item in lista_notas:
    if int(item) < 5:
        lista_calificaciones_alfanumericas.append('Suspenso')
    else:
        lista_calificaciones_alfanumericas.append('Aprobado')

print(lista_calificaciones_alfanumericas)
