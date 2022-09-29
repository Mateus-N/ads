# Ler código dos produtos, quantidade e preço
peca1, quantidade1, valor1 = str ( input ()).split()
peca2, quantidade2, valor2 = str ( input ()).split()

# Armazenar dois valores inteiros e um valor de ponto flutuante com duas casas decimais
peca1 = int ( peca1)
quantidade1 = int ( quantidade1)
valor1 = round ( float ( valor1), 2)

peca2 = int ( peca2)
quantidade2 = int ( quantidade2)
valor2 = round ( float ( valor2), 2)

# Valor total de cada produto
totalPeca1 = quantidade1 * valor1
totalPeca2 = quantidade2 * valor2

# Armazenar total a ser pago
total = totalPeca1 + totalPeca2

# Imprimir total na tela
print (f'VALOR A PAGAR: R$ {total:.2f}')
