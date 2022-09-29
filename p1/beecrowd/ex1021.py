# Ler valor do teclado com ponto flutuante de dupla precisão
valor = round ( float ( input ()), 2)

# Calcular a quantidade de notas de 100
cedulas100 = int (valor // 100)
valor -= cedulas100 * 100

# Calcular a quantidade de notas de 50
cedulas50 = int ( valor // 50)
valor -= cedulas50 * 50

# Calcular a quantidade de notas de 20
cedulas20 = int ( valor // 20)
valor -= cedulas20 * 20

# Calcular a quantidade de notas de 10
cedulas10 = int ( valor // 10)
valor -= cedulas10 * 10

# Calcular a quantidade de notas de 5
cedulas5 = int ( valor // 5)
valor -= cedulas5 * 5

# Calcular a quantidade de notas de 2
cedulas2 = int ( valor // 2)
valor -= cedulas2 * 2

# Calcular a quantidade de moedas de 1 Real
moedas1 = int ( valor // 1)
valor -= moedas1

# Criar a variável centavos e multiplicar o valor por 100 para obter um valor maior que 1
centavos = round (valor * 100, 0)

# Calcular a quantidade de moedas de 50 centavo
centavos50 = int (centavos // 50)
centavos -= centavos50 * 50

# Calcular a quantidade de moedas de 25 centavo
centavos25 = int (centavos // 25)
centavos -= centavos25 * 25

# Calcular a quantidade de moedas de 10 centavo
centavos10 = int (centavos // 10)
centavos -= centavos10 * 10

# Calcular a quantidade de moedas de 5 centavo
centavos5 = int (centavos // 5)
centavos -= centavos5 * 5

# Calcular a quantidade de moedas de 1 centavo
centavos1 = int (centavos // 1)

print (f'''NOTAS:
{cedulas100} nota(s) de R$ 100.00
{cedulas50} nota(s) de R$ 50.00
{cedulas20} nota(s) de R$ 20.00
{cedulas10} nota(s) de R$ 10.00
{cedulas5} nota(s) de R$ 5.00
{cedulas2} nota(s) de R$ 2.00
MOEDAS:
{moedas1} moeda(s) de R$ 1.00
{centavos50} moeda(s) de R$ 0.50
{centavos25} moeda(s) de R$ 0.25
{centavos10} moeda(s) de R$ 0.10
{centavos5} moeda(s) de R$ 0.05
{centavos1} moeda(s) de R$ 0.01''')
