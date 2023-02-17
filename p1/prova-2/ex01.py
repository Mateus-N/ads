# Criacao da fila inicial com 5 valores
ultimo = 5
fila = list(range(1, ultimo + 1))

# imprimir as opcoes na tela
print(
    'Escolha:\n'
    '\t(F) para adicionar um cliente;\n'
    '\t(A) para atender um cliente;\n'
    '\t(C) para consultar a fila; e\n'
    '\t(S) para sair;\n'
)

continuar = True
while continuar:
    # ler as opcoes do teclado em linha unica
    # Remover os espacos
    opcoes = input().upper().replace(' ', '')

    # laco para percorrer todas as opcoes
    for i in range(len(opcoes)):

        # Verificar se opcao == 'F'
        if opcoes[i] == 'F':
            # Incremento do ultimo
            ultimo += 1
            # Adiciona o ultimo na fila
            fila.append(ultimo)
            # Imprimir essa informacao na tela
            print(f'Cliente {ultimo} adicionado na fila.\n')
        
        # Verificar se opcao == 'A'
        elif opcoes[i] == 'A':
            # Tentar remover o primeiro item da fila
            try:
                atendido = fila.pop(0)
                # Imprimir que o cliente foi antendido
                print(f'Cliente {atendido} atendido.\n')
            # Caso a fila esteja vazia
            except IndexError:
                print('Fila vazia! Ninguém para atender.\n')
        
        # Verificar se opcao == 'C'
        elif opcoes[i] == 'C':
            # Imprimir na tela a quantidade de itens na fila
            print(f'Existe(m) {len(fila)} cliente(s) na fila.')
            # Imprimir a fila
            print(f'Fila atual: {fila}\n')
        
        # Verificar se opcao == 'S'
        elif opcoes[i] == 'S':
            # Encerrar o programa
            print('Encerrando o programa...')
            continuar = False
            break

        # Caso não for nenhuma das acima
        else:
            print('Operação inválida!\n')