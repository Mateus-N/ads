coelhos = ratos = sapos = 0

# Ler um valor do teclado
valor = int ( input ())

# Iteração que irá ocorrer na quantidade de vezes do valor
for i in range (0, valor):
  # Ler a quantidade e o tipo da cobaia do teclado
  quantidade, tipo = input().strip().upper().split()

  # Tornar o tipo da quantidade em inteiro
  quantidade = int (quantidade)

  # Verificar se o tipo é coelho
  if tipo == 'C':
    # Adicionar a quantidade a variável coelhos
    coelhos += quantidade
  # Verificar se o tipo é rato
  elif tipo == 'R':
    # Adicionar a quantidade a variável ratos
    ratos += quantidade
  # Verificar se o tipo é sapo
  elif tipo == 'S':
    # Adicionar a quantidade a variável sapos
    sapos += quantidade

# Calcular o total de cobaias
totalDeCobaias = coelhos + ratos + sapos

# Calcular o percentual de cada cobaia em relação ao total
percentualCoelhos = 100 / totalDeCobaias * coelhos
percentualRatos = 100 / totalDeCobaias * ratos
percentualSapos = 100 / totalDeCobaias * sapos

# imprimir todos os dados na tela
print(f'''Total: {totalDeCobaias} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {percentualCoelhos:.2f} %
Percentual de ratos: {percentualRatos:.2f} %
Percentual de sapos: {percentualSapos:.2f} %''')
