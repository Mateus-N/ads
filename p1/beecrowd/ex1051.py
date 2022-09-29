# Ler salario da pessoa no teclado
salario = round ( float ( input ()), 2)

# Verificar se a pessoa é isenta
if salario <= 2000 :
  print ('Isento')

# Verificar se a pessoa está na primeira faixa do imposto
elif salario <= 3000 :
  # Remover a parte isenta
  salario -= 2000
  # Calcular imposto
  imposto = salario / 100 * 8
  # Imprimit imposto na tela
  print (f'R$ {imposto:.2f}')

# Verificar se a pessoa está na segunda faixa do imposto
elif salario <= 4500 :
  # Remover a parte isenta
  salario -= 2000
  # Calcular imposto sobre os 1000 que ficam entre 2000 e 3000
  imposto = 1000 / 100 * 8
  salario -= 1000
  # Calcular imposto sobre a parte acima de 3000
  imposto += salario / 100 * 18
  print (f'R$ {imposto:.2f}')

# Verificar se a pessoa está na terceira faixa do imposto
elif salario > 4500 :
  # Remover a parte isenta
  salario -= 2000
  # Calcular imposto sobre os 1000 que ficam entre 2000 e 3000
  imposto = 1000 / 100 * 8
  salario -= 1000
  # Calcular imposto sobre os 1500 que ficam entre 3000 e 4500
  imposto += 1500 / 100 * 18
  salario -= 1500
  # Calcular imposto sobre a parte que fica acima de 4500
  imposto += salario / 100 * 28
  print (f'R$ {imposto:.2f}')
