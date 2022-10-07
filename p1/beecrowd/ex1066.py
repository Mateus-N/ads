# Declarar variável pares inciando em 0
pares = impares = positivos = negativos = 0

# Iteração que irá ocorrer 5 vezes
for i in range(0, 5):

  # Ler um valor do teclado
  valor = int ( input())

  # Verificar se o valor é par
  if valor % 2 == 0:
    # Adicionar 1 a contagem de pares
    pares += 1
  # Caso contrário
  else:
    # Adicionar 1 a contagem de ímpares
    impares += 1

  # Verificar se o valor é positivo
  if valor > 0:
    # Adicionar 1 a contagem de positivos
    positivos += 1
  # Caso contrário
  elif valor < 0:
    # Adicionar 1 a contagem de negativos
    negativos += 1

# Imprimir todas as variáveis na tela
print(f'''{pares} valor(es) par(es)
{impares} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)''')
