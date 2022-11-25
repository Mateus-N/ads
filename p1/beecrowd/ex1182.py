# Inicio da matriz vazia
matriz = []

# Ler a coluna desejada e a operaçao do teclado
colunaEscolhida = int ( input ())
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

# Inicio da soma em 0
soma = 0
# Laço para realizar a soma da coluna desejada
for i in range(12):
  soma += matriz[i][colunaEscolhida]

# Verificar a operação a ser feita
if opcao == 'S':
  # Imprimir a soma na tela
  print(f'{soma:.1f}')

elif opcao == 'M':
  # Imprimir a média na tela
  print(f'{soma/12:.1f}')
