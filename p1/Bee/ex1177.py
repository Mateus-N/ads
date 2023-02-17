# iniciar lista vazia
n = []

# Ler valor inteiro do teclado
valor = int ( input ())

# Inicio da variavel num em 0
num = 0
# Inicio de iteração em while
while num < 1000:

  # Inicio de iteração com for e range no valor
  for i in range(valor):
    
    # A lista n adiciona a seu final o valor i
    n.append(i)
    # Incremento do num em 1
    num += 1
    # Verificar se o num é maior ou igual de 1000
    if num >= 1000:
      # Fim do laço
      break

# Iteração enumerando os itens da lista
for i, j in enumerate(n):
  # Imprimir os itens da lista na tela
  print(f'N[{i}] = {j}')