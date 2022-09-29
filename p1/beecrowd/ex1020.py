# Ler um valor inteiro do teclado
dias = int ( input ())

# Armazenar a quantidade de anos
ano = dias // 365
dias -= ano * 365

# Armazenar a quantidade de meses
meses = dias // 30
dias -= meses * 30

# Imprimir os valores na tela
print (f'''{ano} ano(s)
{meses} mes(es)
{dias} dia(s)''')
