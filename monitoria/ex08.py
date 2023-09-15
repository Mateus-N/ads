def verificaFizzBuzz(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return "FizzBuzz"

    if valor % 3 == 0:
        return "Fizz"

    if valor % 5 == 0:
        return "Buzz"

    return f"{valor}"


numero = int(input("Digite um número: "))
print(verificaFizzBuzz(numero))
