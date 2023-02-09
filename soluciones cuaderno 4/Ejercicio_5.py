
def calificaciones_alfanumericas(lista_notas):
    """ list --> none
    OBJ: Modifica lista_notas cambiando las notas numéricas por alfanuméricas
    """
    for i in range(len(lista_notas)):
        nota_numerica = lista_notas[i]
        if nota_numerica < 5:
            alfanumerica = 'suspenso'
        elif nota_numerica < 7:
            alfanumerica = 'aprobado'
        elif nota_numerica < 9:
            alfanumerica = 'notable'
        elif nota_numerica <= 10:
            alfanumerica = 'sobresaliente'
        lista_notas[i] = alfanumerica

# Probador
notas = [2.5, 5.5, 6.8, 7.0, 8.5, 9.8, 10]
calificaciones_alfanumericas(notas)
# verifico que realmente he modificado la lista original de notas, tal como se pedia
print(notas)
