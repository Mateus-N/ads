# Receber valor de ponto flututante do teclado
valor = float ( input ())

# Verificar se o valor está fora dos intervalos
if valor < 0 or valor > 100 :
  print ('Fora de intervalo')

# Verificar se valor está entre 0 e 25
elif valor <= 25 :
  print ('Intervalo [0,25]')

# Verificar se valor está entre 25 e 50
elif valor <= 50 :
  print ('Intervalo (25,50]')

# Verificar se valor está entre 50 e 75
elif valor <= 75 :
  print ('Intervalo (50,75]')

# Verificar se valor está entre 75 e 100
else :
  print ('Intervalo (75,100]')
