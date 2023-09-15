def valorANaoEhValido(valor):
    return valor == 0


def calculaDelta(a, b, c):
    return b ** 2 - 4 * a * c


def calculaRaizComDeltaZero(a, b):
    return -b / (2 * a)


def calculaDuasRaizes(a, b, delta):
    raiz1 = (-b + delta ** (1 / 2)) / (2 * a)
    raiz2 = (-b - delta ** (1 / 2)) / (2 * a)
    return raiz1, raiz2


valorA, valorB, valorC = map(float, input().split())
if valorANaoEhValido(valorA):
    print('Impossivel calcular')
else:
    delta = calculaDelta(valorA, valorB, valorC)
    if delta < 0:
        print('Impossivel calcular')
    elif delta == 0:
        print(f'R1 = {calculaRaizComDeltaZero(valorA, valorB):.5f}')
    else:
        x1, x2 = calculaDuasRaizes(valorA, valorB, delta)
        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')