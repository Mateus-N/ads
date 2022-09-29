# Ler quatro valores de dois pontos no plano cartesiano
x1, y1 = str ( input ()).split()
x2, y2 = str ( input ()).split()

# Armazenar os valores específicos dos pontos
x1 = float (x1)
y1 = float (y1)
x2 = float (x2)
y2 = float (y2)

# Armazenar distância entre os pontos
distancia = (( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2 ) ** ( 1 / 2 )

print (f'{distancia:.4f}')
