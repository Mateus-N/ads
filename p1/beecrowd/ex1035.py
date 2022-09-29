# Ler quatro valores
valorA, valorB, valorC, valorD = str ( input ()).split()

# Receber os valores como inteiros
valorA = int (valorA)
valorB = int (valorB)
valorC = int (valorC)
valorD = int (valorD)

# Imprimir na tela se os valores são aceitos
if valorB > valorC and valorD > valorA and valorC + valorD > valorA + valorB and valorC >= 0 and valorD >= 0 and valorA % 2 == 0:
  print ('Valores aceitos')
else :
  print ('Valores nao aceitos')
