# Ler salario atual do teclado
salarioAtual =  round ( float ( input ()), 2)

# Verificar se o salario é menor ou igual 400
if salarioAtual <= 400 :
  # Calcular novo salário
  salarioNovo = salarioAtual / 100 * 115
  # Calcular reajuste
  reajuste = salarioNovo - salarioAtual
  # Armazenar percentual
  percentual = '15'

# Verificar se o salario é menor ou igual 800
elif salarioAtual <= 800 :
  # Calcular novo salário
  salarioNovo = salarioAtual / 100 * 112
  # Calcular reajuste
  reajuste = salarioNovo - salarioAtual
  # Armazenar percentual
  percentual = '12'

# Verificar se o salario é menor ou igual 1200
elif salarioAtual <= 1200 :
  # Calcular novo salário
  salarioNovo = salarioAtual / 100 * 110
  # Calcular reajuste
  reajuste = salarioNovo - salarioAtual
  # Armazenar percentual
  percentual = '10'

# Verificar se o salario é menor ou igual 2000
elif salarioAtual <= 2000 :
  # Calcular novo salário
  salarioNovo = salarioAtual / 100 * 107
  # Calcular reajuste
  reajuste = salarioNovo - salarioAtual
  # Armazenar percentual
  percentual = '7'

# Caso nenhuma das opções acima forem verdade o salario e maior que 2000
elif salarioAtual > 2000 :
  # Calcular novo salário
  salarioNovo = salarioAtual / 100 * 104
  # Calcular reajuste
  reajuste = salarioNovo - salarioAtual
  # Armazenar percentual
  percentual = '4'

print (f'''Novo salario: {salarioNovo:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: {percentual} %''')
