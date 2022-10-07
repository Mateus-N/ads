# Ler um valor do teclado
valor = int ( input ())

# Iteração que irá ocorrer na quantidade de vezes do valor
for i in range (0, valor):
  # Ler três valos de ponto flutuante do teclado
  notaA, notaB, notaC = map(float, input().split())

  # Adicionar a cada nota seu peso
  notaA = notaA * 2
  notaB = notaB * 3
  notaC = notaC * 5

  # Calcular a média ponderada das notas
  media = (notaA + notaB + notaC) / 10

  # Imprimir media na tela com uma casa decimal
  print(f'{media:.1f}')