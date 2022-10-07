# Ler um valor do teclado
valor = int ( input ())

# Iteração que irá ocorrer na quantidade de vezes do valor
for i in range (0, valor):
  # Ler o dividendo e o divisor do teclado
  dividendo, divisor = map (int, input().split())

  # Verificar se o divisor é 0
  if divisor == 0:
    # Imprimir divisao impossivel
    print('divisao impossivel')
  # Caso contrário
  else:
    # Calcular o resultado da divisão
    resultado = dividendo / divisor
    # Imprimir na tela o resultado com uma casa decimal
    print(f'{resultado:.1f}')
