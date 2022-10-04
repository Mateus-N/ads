# Declaração do contador iniciando em 0
contador = 0

# Ler um valor inteiro do teclado
valor = int ( input ())

# Iteração que irá ocorrer enquanto o contador
# for menor ou igual que 10000
while contador <= 10000:

  # Incremento do contador em 1
  contador += 1
  # Verificar se o resto da divisão do contador
  # pelo valor valor deixa resto 2
  if contador % valor == 2:
    # Caso sim imprimir o contador na tela
    print (contador)
