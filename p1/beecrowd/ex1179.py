# Inicio das listas par e impar
par = []
impar = []

# Laço para receber os 15 valores
for i in range(15):
  # Ler um valor do teclado
  valor = int ( input ())

  # Verificar se o valor é par
  if valor % 2 == 0:
    # Adicionar o valor na lista de pares
    par.append(valor)
  else:
    # Adicionar na lista de impares
    impar.append(valor)
  
  # Verificar se a lista impar tem 5 itens ou o final do laço
  if len(impar) == 5 or i == 14:
    # Laço para imprimir os itens na tela
    for indice, valor in enumerate(impar):
      # Imprimir na tela junto ao indice
      print(f'impar[{indice}] = {valor}')

    # Limpa a lista de impares
    impar = []

  # Verificar se a lista par tem 5 itens ou o final do laço
  if len(par) == 5 or i == 14:
    # Laço para imprimir os itens na tela
    for indice, valor in enumerate(par):
      # Imprimir na tela junto ao indice
      print(f'par[{indice}] = {valor}')

    # Limpar a lista de pares
    par = []
