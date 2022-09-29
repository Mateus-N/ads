def main():
  a, b, c = str ( input ()).split()
  a = float (a)
  b = float (b)
  c = float (c)
  if a != 0 :
    delta = calcularDelta(a, b, c)
    if delta >= 0 :
      r1, r2 = bhaskara(a, b, delta)
      if r1 == r2:
        imprimir(f'R1 = {r1:.5f}')
      else:
        imprimir(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
    else:
      imprimir('Impossivel calcular')
  else:
    imprimir('Impossivel calcular')


def calcularDelta(a, b, c):
  return (b ** 2 - 4 * a * c)


def bhaskara(a, b , delta):
  r1 = (-b + delta ** ( 1 / 2 )) / (2 * a)
  r2 = (-b - delta ** ( 1 / 2 )) / (2 * a)
  return r1, r2


def imprimir(frase):
  print(frase)


main()
