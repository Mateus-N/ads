# Ler distância total em Km
distancia = int ( input ())

# Ler total de combustível gasto com uma casa decimal
totalGasto = round ( float ( input ()), 1)

# Calcular consumo médio
consumo = distancia / totalGasto

# Imprimir a distância na tela
print (f'{consumo:.3f} km/l')
