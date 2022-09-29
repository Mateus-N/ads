#Ler três valores no teclado
valorA, valorB, valorC = str ( input ()).split()

# Receber valores inteiros
valorA = int (valorA)
valorB = int (valorB)
valorC = int (valorC)

# Verificar qual o maior valor entre A e B
maiorAB = ( valorA + valorB + abs( valorA - valorB )) / 2
# Verificar o maior entre o maior entre A, B e C
maiorABC = ( maiorAB + valorC + abs( maiorAB - valorC )) / 2

# Imprimir na tela o maior valor
print (f'{maiorABC:.0f} eh o maior')
