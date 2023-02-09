def comando_resultado(cad):
    """string->list
    OBJ: Devuelve una lista de tuplas con el código y resultado de cada comando
    PRE: La cadena no está vacía y contiene comandos en el formato apropiado"""
    l=[]
    comandos=cad.split('.')
    for comando in comandos:
        partes=comando.split()
        par=(partes[0],partes[3])
        l.append(par)
    return (l)

comandos= 'SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. OR A B FALSE'
if comandos !='':
    print(comando_resultado(comandos))
else: 
    print('La cadena de comandos está vacía')
