# Ler dois valores do teclado
valorA, valorB = str ( input ()).split()

# Armazenar como inteiros
valorA = int (valorA)
valorB = int (valorB)

# Verificar se são multiplos
if valorA % valorB == 0 or valorB % valorA == 0 :
  print ('Sao Multiplos')
else :
  print ('Nao sao Multiplos')
