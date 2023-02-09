# Un texto contiene comandos en forma de frases separadas por puntos. En cada 
# frase,  la  primera  palabra  contiene  el  código  de  la  operación  y  la  última  el 
# resultado. Ejemplo:   
  
# SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200. Etc.  
  
# Cree  una  lista  de  parejas  [código-resultado] utilizando  como entrada un texto 
# con el formato indicado.

def comandos(frase):
    """ str --> list
        OBJ: pasa los comandos y resultados de una frase de comandos a una lista.
    """
    lista_frase = frase.split('.')
    print(lista_frase)
    comandos = []
    partes_ini = []
    partes_fin = []
    for x in range(len(lista_frase)):
        comandos.append(lista_frase[x].split())
    print(comandos)
    for i in range(len(comandos)):
        partes_ini.append(comandos[i][:1])
        partes_fin.append(comandos[i][3:])
    print(partes_ini)
    print(partes_fin)
    for a in range(len(partes_ini)):
        resultado = partes_ini[a] + partes_fin[a]
    
    print(resultado)
frase = 'SUMAR 45 50 95. AND A B TRUE. MULT 10 20 200'
comandos(frase)



def comando_final(cadena):
    """ srt --> list
        OBJ: pasa los comandos y resultados de una frase de comandos a una lista.
    """
    resultado = []
    comandos = cadena.split('.')
    for comando in comandos:
        partes = comando.split()
        par = (partes[0], partes[3])
        resultado.append(par)
    print(resultado)

comando_final(frase)