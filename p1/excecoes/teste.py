def leiaInt(pergunta):
    while True:
        try:
            valor = int ( input (pergunta))
        except ValueError:
            print('Digite um valor válido')
        except KeyboardInterrupt:
            continue
        else:
            return valor


numero = leiaInt('\nDigite um número: ')

print(numero)
