# Ler duas notas de um aluno com valores de ponto flutuante de dupla precisão
primeiraNota = round ( float ( input ()), 2)
segundaNota = round ( float ( input ()), 2)

# Calcular peso das notas para média ponderada
# primeiraNota tem peso 3.5
# segundaNota tem peso 7.5
pesoPrimeiraNota = primeiraNota * 3.5
pesoSegundaNota = segundaNota * 7.5

# Calcular média ponderada
media = ( pesoPrimeiraNota + pesoSegundaNota ) / 11

# Imprimir média na tela
print (f'MEDIA = {media:.5f}')
