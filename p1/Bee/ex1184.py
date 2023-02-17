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


# Inicio da soma e do contador em 0
soma = cont = 0

# Laço duplo para percorrer toda a matriz
for i in range(12):
  for j in range(12):

    # Caso j < i se trata da parte de baixo da matriz
    if j < i:
      # Adiciona o valor da celula a soma e incrementa o contador em 1
      soma += matriz[i][j]
      cont += 1


# Verificar a operação a ser feita
if opcao == 'S':
  # Imprimir a soma na tela
  print(f'{soma:.1f}')

elif opcao == 'M':
  # Imprimir a média na tela
  print(f'{soma/cont:.1f}')