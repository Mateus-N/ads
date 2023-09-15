def receberValores():
    valorA = float(input('Digite o valor de A: '))
    valorB = float(input('Digite o valor de B: '))
    valorC = float(input('Digite o valor de C: '))
    if valorA == 0:
        print('O valor de "A" não pode ser 0, digite os valores novamente!')
        return receberValores()
    return valorA, valorB, valorC


def calculaDelta(a, b, c):
    return (b ** 2) - (4 * a * c)


def calculaRaizCasoDeltaIgualZero(a, b, delta):
    return (-b) / (2 * a)


def calculaRaizParaDeltaMaiorQueZero(a, b, delta):
    x1 = (-b + (delta * (1/2))) / (2 * a)
    x2 = (-b - (delta * (1/2))) / (2 * a)
    return x1, x2


def main():
    a, b, c = receberValores()
    delta = calculaDelta(a, b, c)
    if delta < 0:
        print('Essa equação não possuí raizes reais')
    elif delta == 0:
        x = calculaRaizCasoDeltaIgualZero(a, b, delta)
        print(f'A raiz da enquação é {x}')
    else:
        x1, x2 = calculaRaizParaDeltaMaiorQueZero(a, b, delta)
        print(f'As raizes da equação são x1={x1} e x2={x2}')


main()
