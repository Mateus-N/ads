# Ler do teclado a quantidade 
# de vezes que a iteração vai acontecer
repeticoes = int ( input ())

# Iteração que ocorre enquanto repeticoes for maior que 0
while repeticoes > 0:
  
  # Ler dois valores inteiros do teclado
  valor1, valor2 = map(int, str( input ()).split())

  # Verificar se o primeiro valor é maior que o segundo
  if valor1 > valor2:
    # Variável auxiliar para armazenar o valor1
    aux = valor1
    # Valor1 agora recebe valor2
    valor1 = valor2
    # Valor2 recebe o valor1 que estava na variável auxiliar
    valor2 = aux
  
  # Declaração de variável que a cada iteração volta a 0
  somaImpares = 0
  # Incremento do valor1 pois os extremos do intervalo não contam
  valor1 += 1

  # Iteração que vai ocorrer enquanto
  # valor1 for menor que valor2
  while valor1 < valor2:

    # Verificar se valor1 é ímpar
    if valor1 % 2 == 1:
      # Caso sim ele é somado a somaImpares
      somaImpares += valor1
    # Incremento do valor1 em 1
    valor1 += 1
  
  # Decremento de repeticoes
  repeticoes -= 1
  # imprimir somaImpares na tela
  print(somaImpares)
