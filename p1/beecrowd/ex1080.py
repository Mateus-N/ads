# Declaração das variáveis, todas iniciando em 0
contador = 0
maior = 0
posicaoMaior = 0

# Iteração que irá ocorrer enquanto o contador
# for menor que 100
while contador < 100:

  # incremento do contador em 1
  contador += 1
  # Ler um valor inteiro do teclado
  valor = int ( input ())
  # Verificar se o valor é o maior digitado até o momento
  if valor > maior:
    # Caso sim a variável maior recebe o valor
    maior = valor
    # E a posicaoMaior recebe o contador
    posicaoMaior = contador

# Imprimir na tela o maior valor e a posição dele
print(f'''{maior}
{posicaoMaior}''')
