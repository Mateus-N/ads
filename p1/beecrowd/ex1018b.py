# ler um valor inteiro do teclado
valor = int ( input ())
# Imprimir o valor na tela
print (valor)

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

# Calcular a quantidade de notas de 1
cedulas1 = valor

# Imprimir na tela a quantidade de todas as cedulas
print (f'''{cedulas100} nota(s) de R$ 100,00
{cedulas50} nota(s) de R$ 50,00
{cedulas20} nota(s) de R$ 20,00
{cedulas10} nota(s) de R$ 10,00
{cedulas5} nota(s) de R$ 5,00
{cedulas2} nota(s) de R$ 2,00
{cedulas1} nota(s) de R$ 1,00''')
