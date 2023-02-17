# Inicio da matriz vazia
matriz = []

# Ler operação desejada do teclado
opcao = input().upper()

# Laço para preencher a matriz
for i in range(12):
  # Lista vazia para preencher a linha
  prencherLinha = []

  # Laço para preencher a linha
  for j in range(12):
    # Ler valor do teclado
    valor = float ( input ())
    # Adicionar valor a linha
    prencherLinha.append(valor)
  
  # Adicionar linha a matriz
  matriz.append(prencherLinha[:])

# Limite que será usado para o for interior da matriz
limite = 11
# Inicio da soma e do total de valores
soma = totalSomados = 0

# Laço para a primeira dimensão da matriz
for i in range(11):
  # Laço para a segunda dimensão que vai até o limite
  for j in range(limite):
    # Soma o valor na matriz na posição i, j
    soma += matriz[i][j]
    # Incrementa o total de somados
    totalSomados += 1
  
  # Decremento do limite
  limite -= 1

# Verificar a operação a ser feita
if opcao == 'S':
  # Imprimir a soma na tela
  print(f'{soma:.1f}')

elif opcao == 'M':
  # Imprimir a média na tela
  print(f'{soma/totalSomados:.1f}')
