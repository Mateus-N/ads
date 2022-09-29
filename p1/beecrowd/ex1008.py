# Ler número do funcionário
numeroFuncionario = int ( input ())

# Ler número de horas trabalhadas
horasTrabalhadas = int ( input ())

# Ler salário por hora
salarioPorHora = float ( input ())

# Calcular valor a receber
salario = horasTrabalhadas * salarioPorHora

# Mostrar número do funcionário e valor a receber na tela
print (f'''NUMBER = {numeroFuncionario}
SALARY = U$ {salario:.2f}''')
