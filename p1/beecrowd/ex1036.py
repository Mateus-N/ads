# Ler três valores no teclado
valorA, valorB, valorC = str ( input ()).split()

# Receber os valores como float
valorA = float (valorA)
valorB = float (valorB)
valorC = float (valorC)

# Se A for 0 a raiz é impossível pois vai ser necessário divir por 0
if valorA == 0 :
  print ('Impossivel calcular')

else :
  # Armazenar o valor de delta
  delta = valorB ** 2 - 4 * valorA * valorC

  # Caso delta menor que zero a raiz é impossível pois vai ser necessário calcular a raiz de um número negativo
  if delta < 0 :
    print ('Impossivel calcular')

  else :
    # Armazenar a raiz de delta
    delta = delta ** (1/2)
    # Calcular a primeira raiz
    raiz1 = ((valorB * -1) + delta ) / (2 * valorA)
    # Calcular a segunda raiz
    raiz2 = ((valorB * -1) - delta ) / (2 * valorA)
    # Imprimir as raizes na tela
    print (f'''R1 = {raiz1:.5f}\nR2 = {raiz2:.5f}''')
