def temNumerosNaMesmaLinhaOuColuna(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            # verifica se tem igual na mesma linha
            if matriz[i].count(matriz[i][j]) > 1:
                return True
            
            # verifica se tem igual na mesma coluna
            repeticoesNaColuna = 0
            for k in range(len(matriz)):
                if matriz[k][j] == matriz[i][j]:
                    repeticoesNaColuna += 1

                if repeticoesNaColuna > 1:
                    return True

    return False


def imprimirMatriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f' {valor:<4} ', end='|')
        print()


tamanho = 5
matriz = []
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        valor = int (input(f'Digite um valor para a posição {i}, {j}: '))
        linha.append(valor)
    matriz.append(linha)

print()
imprimirMatriz(matriz)
print()
print(temNumerosNaMesmaLinhaOuColuna(matriz))
