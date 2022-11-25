# Ler o tamanho da lista do teclado
valor = int ( input ())

# Ler a lista na mesma linha
valores = input().split()

for i in range(len(valores)):
  valores[i] = int(valores[i])

menor = valores[0]
posicao = 0

# Laço que percorre o range do valor
for i, j in enumerate(valores):

  # Caso o valor na posição i for menor que o menor
  if j <= menor:
    # menor recebe valor na posição i
    menor = j
    # Posição recebe i
    posicao = i

# Imprimir o menor e a posição na tela
print(f'''Menor valor: {menor}
Posicao: {posicao}''')
