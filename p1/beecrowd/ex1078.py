# Ler um valor do teclado
valor = int ( input ())

# Iteração que irá ocorrer 10 vezes
for i in range(0, 10):
  # Imprimir o i + 1, o valor e a multiplicação do i + 1 pelo valor
  print(f'{i + 1} x {valor} = {(i + 1) * valor}')
