def receberValores ():
  while True:

    a, b, c = map (float, input('Digite os valores de A, B e C: ').split())

    while a == 0:
      a = float ( input('Valor de A não pode ser 0 digite novamente o A: '))
    
    d = delta(a, b, c)

    if d >= 0:
      break
    else:
      print('O valor de delta não pode ser negativo, Digite novos valores')

  return a, b, d


def delta(a, b, c):
  return b**2 - 4 * a * c


def bhaskara(a, b, delta):
  r1 = (-b + delta ** ( 1 / 2 )) / (2 * a)
  r2 = (-b - delta ** ( 1 / 2 )) / (2 * a)
  return r1, r2


def main():
  a, b, d = receberValores()

  r1, r2 = bhaskara(a, b, d)

  if r1 == r2:
    print(f'R1 = {r1:.5f}')
  else:
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')


main()
