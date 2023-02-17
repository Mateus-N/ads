def fib(vezes, valorA = 0, valorB = 1):

    if vezes == 1:
        return valorA
    
    aux = valorA
    valorA = valorB
    valorB += aux

    return fib(vezes - 1, valorA, valorB)


def fatorial(num):
    if num < 2:
        return 1
    return num * fatorial(num - 1)


termo = int ( input ('Qual o termo? '))
print(fib(termo))
print(fatorial(termo))
