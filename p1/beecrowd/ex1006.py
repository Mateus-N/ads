# Ler três notas de um aluno
primeiraNota = float ( input ())
segundaNota = float ( input ())
terceiraNota = float ( input ())

# Calcular peso das notas
# primeiraNota tem peso 2
# segundaNota tem peso 3
# terceiraNota tem peso 5
pesoPrimeiraNota = primeiraNota * 2
pesoSegundaNota = segundaNota * 3
pesoTerceiraNota = terceiraNota * 5

# Calcular média ponderada
media = ( pesoPrimeiraNota + pesoSegundaNota + pesoTerceiraNota ) / 10

# imprimir média na tela
print (f'MEDIA = {media:.1f}')
