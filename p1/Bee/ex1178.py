# Inicio do vetor n vazio
n = []

# Ler um valor de ponto flutuante do teclado
valor = float ( input ())

# Limitar o valor lido a 4 casas decimais
valor = round(valor, 4)

# Inicio de laço em for no range de 100
for i in range(100):
  # O vetor n apenda o valor
  n.append(valor)
  # O valor é dividido por 2
  valor /= 2

# Iteração enumerando os itens da lista
for i, j in enumerate(n):
  # Imprimir os itens da lista na tela
  print(f'N[{i}] = {j:.4f}')