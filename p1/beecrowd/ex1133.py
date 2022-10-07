# Receber dois valores inteiros do teclado
valorA = int ( input ())
valorB = int ( input ())

# Verificar se o valorA é maior que valorB
if valorA > valorB:
  # A variável auxiliar armazena valorA
  aux = valorA
  # ValorA recebe valorB
  valorA = valorB
  # valorB recebe valorA que estava em aux
  valorB = aux

# Laço que irá percorrer todo o intervalo
# Ignorando os extremos
for i in range(valorA + 1, valorB):

  # Verificar se o resto da divisão de i por 5 é 2 ou 3
  if i % 5 == 2 or i % 5 == 3:
    # Caso sim imprimir i na tela
    print(i)