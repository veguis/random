
LONGITUD_MAX = 25
longitudes = [0] * LONGITUD_MAX

palabra = input(f'Introduzca una palabra: ')
while palabra != 'fin':
    if len(palabra) > 0 and len(palabra) <= LONGITUD_MAX:
        longitudes[len(palabra) - 1] += 1
    else:
        print(f'Error: La longitud de la palabra debe ser mayor que 0 y menor o igual que {LONGITUD_MAX}')
    palabra = input(f'Introduzca una palabra: ')

for i in range(LONGITUD_MAX):
    if longitudes[i] > 0:
        print(f'Palabras de longitud {i + 1}: {longitudes[i]}')
