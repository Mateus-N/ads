# Declarar variável soma
soma = 0

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
  # Verificar se o valor do laço é impar
  if i % 2 == 1:
    # Somar o valor a vairiável soma
    soma += i

print(soma)