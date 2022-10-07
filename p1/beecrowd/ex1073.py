# Ler um valor inteiro do teclado
valor = int ( input ())

# Laço que irá percorrer valores
# Iniciando em 2, indo até o valor e com passo 2
for i in range(2, valor + 1, 2):
  # Imprimir o valor e o resultado de seu quadrado na tela
  print(f'{i}^2 = {i ** 2}')
