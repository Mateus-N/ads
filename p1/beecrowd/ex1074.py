# Ler um valor inteiro do teclado
valor = int ( input ())

# Laço que irá começar 0, indo até o valor - 1
for i in range(0, valor):

  # Ler um valor inteiro do teclado
  numero = int ( input ())
  
  # Verificar se o valor é 0
  if numero == 0:
    # Imprimir NULL na tela
    print('NULL')
  # Verificar se o valor é par
  elif numero % 2 == 0:
    # Imprimir EVEN na tela e deixar o próximo print na mesma linha
    print('EVEN', end=' ')
  # Verificar se o valor é impar
  elif numero % 2 == 1:
    # Imprimir ODD na tela
    print('ODD', end=' ')

  # Verificar se o numero é positivo
  if numero > 0:
    # Imprimir POSITIVE na tela e deixar o próximo print na mesma linha
    print('POSITIVE')
  # Verificar se o número é negativo
  elif numero < 0:
    # Imprimir NEGATIVE na tela
    print('NEGATIVE')
