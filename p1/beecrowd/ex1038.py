# Ler o código do produto e quantidade
codigo, quantidade = str ( input ()).split()

# Armazenar os valores como inteiros
codigo = int (codigo)
quantidade = int (quantidade)

# Calcular valor a ser pago
# Se produto 1
if codigo == 1 :
  total = quantidade * 4.0

# Se produto 2
elif codigo == 2 :
  total = quantidade * 4.5

# Se produto 3
elif codigo == 3 :
  total = quantidade * 5.0

# Se produto 4
elif codigo == 4 :
  total = quantidade * 2.0

# Se produto 5
elif codigo == 5 :
  total = quantidade * 1.5

# Imprimir total na tela
print (f'Total: R$ {total:.2f}')
