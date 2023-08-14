# Funcao para imprimir o dicionario na tela
def imprimirDicionario(dic):
    print()

    # Variavel para guardar o valor total pago
    totalPago = 0

    # Laco para percorrer todo o dicionario
    for fruta in dic:
        # calcular o total pago por item
        totalPorItem = dic[fruta][0] * dic[fruta][1]
        # Adicionar o total do item ao total pago
        totalPago += totalPorItem
        # Criar a linha que sera impressa
        linha = f'{fruta} x \t {dic[fruta][0]}   {dic[fruta][1]:.2f}   {totalPorItem:.2f}'
        # imprimir linha
        print(linha)
    
    # Laco para imprimir linha de '-'
    for i in range(len(linha) + 5):
        print('-', end='')
    print()
    # imprimir o total pago na tela
    print(f'Total: {totalPago:.2f}')


# iniciar dicionario vazio
listaDeFrutas = {}

# laco para receber as frutas
while True:
    # Receber produto do teclado
    produto = input('Produto: ')

    # verificar se deseja encerrar o laco
    if produto.lower() == 'fim':
        break

    # Tentar receber a quantidade e o valor do teclado
    try:
        quantidade = int ( input ('Quantidade: '))
        valor = float ( input ('Valor: '))
    # Caso o valor não seja aceito
    except ValueError:
        print('Valor inválido\n')
    # Caso o valor for aceito
    else:
        # Adicionar espaços ao final do nome do produto
        while len(produto) < 25:
            produto += ' '

        # Adiconar valores ao dicionario
        listaDeFrutas[produto] = [quantidade, valor]

# Imprimir dicionario na tela
imprimirDicionario(listaDeFrutas)