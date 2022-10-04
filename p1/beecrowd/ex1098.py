# Declaração da variáveis
i = 0
j = 1

# Iteração que irá ocorrer enquanto
# i for menor ou igual a 2
while i <= 2:

  # Criação do contador que a cada iteração volta a 0
  contador = 0

  # Iteração que irá ocorrer enquanto
  # o contador for menor que 3
  while contador < 3:

    # Verificar se i é um número inteiro
    if i == 0 or i == 1 or i == 2:
      # Caso sim imprimir i e j sem as casas decimais
      print(f'I={i:.0f} J={j:.0f}')

    else:
      # Caso contrário imprimir i e j com uma casa decimal
      print(f'I={i:.1f} J={j:.1f}')

    # Incremento do j e do contador em 1
    j += 1
    contador += 1
  
  # Incremento do i em 0.2
  # Fixando para apenas uma casa decimal
  i = round(i + 0.2, 1)
  # j recebendo o valor de i somado a 1
  # Fixando para apenas uma casa decimal
  j = round(i + 1, 1)
