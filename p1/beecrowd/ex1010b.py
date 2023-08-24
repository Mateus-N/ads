# Ler código dos produtos, quantidade e preço
_, quantidade1, valor1 = input().split()
_, quantidade2, valor2 = input().split()

# Armazenar dois valores inteiros e um valor de ponto flutuante com duas casas decimais
quantidade1 = int (quantidade1)
valor1 = round ( float ( valor1), 2)

quantidade2 = int ( quantidade2)
valor2 = round ( float ( valor2), 2)

# Valor total de cada produto
totalPeca1 = quantidade1 * valor1
totalPeca2 = quantidade2 * valor2

# Armazenar total a ser pago
total = totalPeca1 + totalPeca2

# Imprimir total na tela
print (f'VALOR A PAGAR: R$ {total:.2f}')
