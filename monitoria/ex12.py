import os

def soma(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'


def subtracao(num1, num2):
    return f'{num1} - {num2} = {num1 - num2}'


def multiplicacao(num1, num2):
    return f'{num1} x {num2} = {num1 * num2}'


def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero."
    return f'{num1} ÷ {num2} = {num1 // num2}'


def querContinuar():
    continuar = input('Quer executar novamente? sim ou não? ')
    if continuar[0] == 's':
        os.system('cls')
        return False
    elif continuar[0] == 'n':
        return True
    else:
        print('Não entendi!')
        querContinuar()


while True:
    num1 = int(input("Digite o primeiro número: "))
    entrada = input("Digite a operação (+, -, x, /): ")
    num2 = int(input("Digite o segundo número: "))

    if entrada == '+':
        print(soma(num1, num2))
    elif entrada == '-':
        print(subtracao(num1, num2))
    elif entrada == 'x':
        print(multiplicacao(num1, num2))
    elif entrada == '/':
        print(divisao(num1, num2))
    else:
        print("Operação inválida!")

    if querContinuar():
        break


print('Obrigado volte sempre!')