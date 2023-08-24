# Declarar variável de valor a ser pago
totalPago = 0

# Iteração para pedir informações dos dois produtos
for i in range ( 0, 2 ) :

  # Ler informações do teclado e armazenar numa lista
  produto = input ().split()

  # Atribuir às variáveis o valor e a quantidade de peças
  quantidade = int ( produto[1])
  valor = float ( produto[2])

  # Armazenar valor a pagar pelo item
  totalItem = quantidade * valor

  # Total a pagar
  totalPago += totalItem
  
print (f'VALOR A PAGAR: R$ {totalPago:.2f}')
