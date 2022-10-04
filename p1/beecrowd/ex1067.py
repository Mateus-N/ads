# Declaração do contador iniciando em 1
# por ser o primeiro inteiro positivo ímpar
contador = 1

# Ler um valor do teclado e armazenar em uma variável
valor = int ( input ())

# Inicio de iteração que irá se repetir enquanto
# o contador for menor que o valor digitado
while contador <= valor:

  # Imprimir o contador na tela
  print(contador)
  # Incremento do contador a cada iteração
  # é adicionado 2 para que o contador permaneca ímpar
  contador += 2
