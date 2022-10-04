# Inicio de iteração utilizando True
while True:
  # Ler dois valores inteiros do teclado
  valor1, valor2 = map(int, str ( input ()).split())

  # Caso qualquer um dos valores for
  # 0 ou negativo encerrar a iteração
  if valor1 <= 0 or valor2 <= 0:
    break

  # Verificar se o primeiro valor é maior que o segundo
  if valor1 > valor2:
    # Variável auxiliar para armazenar o valor1
    aux = valor1
    # Valor1 agora recebe valor2
    valor1 = valor2
    # Valor2 recebe o valor1 que estava na variável auxiliar
    valor2 = aux

  # Declaração da variável somaValores
  # A cada iteração ela volta a 0
  somaValores = 0

  # Iteração que vai ocorrer enquanto
  # valor1 for menor ou igual a valor2
  while valor1 <= valor2:

    # Imprimir valor1 na tela continuando
    # o próximo print na mesma linha
    print(valor1, end=' ')
    # Somar valor1 ao total de somaValores
    somaValores += valor1
    # Incremento de valor1 em 1
    valor1 += 1
  
  # Imprimir somaValores na tela
  print(f'Sum={somaValores}')
