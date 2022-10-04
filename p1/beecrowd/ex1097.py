# Declaração da variável i iniciando em 1
i = 1
# Declaração da variável j inicando em 7
j = 7

# Iteração que irá ocorrer enquanto
# i for menor ou igual que 9
while i <= 9:
  
  # Declaração da variável parada
  # que a cada iteração recebe o valor de j - 2
  parada = j - 2

  # Iteração que irá ocorrer enquanto
  # j for maior ou igual a parada
  while j >= parada:

    # Imprimir i e j na tela
    print (f'I={i} J={j}')
    # decremento do j em 1
    j -= 1

  # incremento do i em 2
  i += 2
  # incremento do j em 5
  j += 5
