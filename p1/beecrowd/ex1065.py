# Declarar variável pares inciando em 0
pares = 0

# Iteração que irá ocorrer 5 vezes
for i in range(0, 5):

  # Ler um valor do teclado
  valor = int ( input())
  # Verificar se o valor é par
  if valor % 2 == 0:
    # Adicionar 1 a contagem de pares
    pares += 1

# Imprimir a quantidade de pares na tela
print(f'{pares} valores pares')
