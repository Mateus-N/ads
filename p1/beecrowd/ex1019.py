# Ler um valor inteiro do teclado
segundos = int ( input ())

# Amazenar a quantidade de minutos
minutos = segundos // 60
segundos -= minutos * 60

# Armazenar a quaintodade de horas
horas = minutos // 60
minutos -= horas * 60

# Imprimir os valores na tela
print (f'{horas}:{minutos}:{segundos}')
