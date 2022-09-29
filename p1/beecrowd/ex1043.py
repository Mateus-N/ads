# Ler três valores do teclado
valorA, valorB, valorC = str ( input ()).split()

# Armazenar os valores como float
valorA = float (valorA)
valorB = float (valorB)
valorC = float (valorC)

# Verificar se formam um triângulo
if valorA + valorB > valorC and valorA + valorC > valorB and valorB + valorC > valorA :

  # Calcular o perimetro do triângulo
  perimetro = valorA + valorB + valorC
  print (f'Perimetro = {perimetro:.1f}')

# Caso contrário calcular área do trapezio
else :

  area = ((valorA + valorB) * valorC ) / 2
  print (f'Area = {area:.1f}')
