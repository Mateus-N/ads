# ler tempo da viagem em H e a velocidade média em Km/h
tempo = int ( input ())
velocidade = int ( input ())

# Armazenar distância
distancia = tempo * velocidade

# Calcular gasto de combustível considerando 12 Km/l
gasto = distancia / 12

# Imprimir gasto na tela
print (f'{gasto:.3f}')
