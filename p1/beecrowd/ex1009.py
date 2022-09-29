# Ler nome do vendedor
nomeVendedor = str ( input ())

# Ler salário fixo
salarioFixo = float ( input ())

# Ler total de vendas no mês
vendas = float ( input ())

# Calcular comissão de 15% a receber pelas vendas
comissao = vendas / 100 * 15

# Calcular total a receber
totalReceber = salarioFixo + comissao

# Imprimir total a receber na tela
print (f'TOTAL = R$ {totalReceber:.2f}')
