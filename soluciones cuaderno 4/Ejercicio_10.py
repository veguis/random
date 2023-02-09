
codigos = {'a': '4', 
           'e': '3', 
           'i': '1', 
           'o': '0', 
           'u': '#'}

cadena = 'Un perro del hortelano'
resul = ''
for letra in cadena:
    minusculas = letra.lower()
    if minusculas in codigos:
        resul += codigos[minusculas]
    else:
        resul += letra
print(resul)
