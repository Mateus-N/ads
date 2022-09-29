def entrada ():
  x1, y1 = map(float, input().split())
  x2, y2 = map(float, input().split())
  valor = distancia(x1, x2, y1, y2)
  imprimir(valor)


def distancia(x1, x2, y1, y2) :
  distancia = ( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2
  distancia = raiz(distancia)
  return distancia


def raiz(valor) :
  raiz = valor ** (1/2)
  return raiz


def imprimir(valor):
  print(f'{valor:.4f}')


entrada()
