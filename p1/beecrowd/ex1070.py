# Declaração do contador da iteração
# Iniciando em 0
contador = 0

# Ler um número inteiro do teclado
valor = int ( input ())

# Inicio da iteração que irá se repetir enquanto
# o contador for menor que 6
while contador < 6:

  # Verificar se o valor é ímpar
  if valor % 2 == 1:
    # Caso sim, imprimir o valor na tela
    print(valor)
    # Incremento do contado em 1
    contador += 1

  # Incremento do valor em 1
  valor += 1

