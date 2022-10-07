# Declarar variável positivos inciando em 0
positivos = 0

# Iteração que irá ocorrer 6 vezes
for i in range(0, 6):

  # Ler um valor do teclado
  valor = float ( input())
  # Verificar se o valor é positivo
  if valor >= 0:
    # Adicionar 1 a contagem de positivos
    positivos += 1

# Imprimir a quantidade de positivos na tela
print(f'{positivos} valores positivos')
