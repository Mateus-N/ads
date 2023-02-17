arquivo = open('linhas.txt', 'w')

for linha in range(10):
 arquivo.write(f'{linha + 1} linha\n')

arquivo.close()

arquivo = open('linhas.txt', 'r')

salvarArquivo = []
for linha in arquivo.readlines():
  salvarArquivo.append(linha[:-1])

arquivo.close()

arquivo = open('linhas.txt', 'w')

for linha in range(10):
  arquivo.write(salvarArquivo[linha] + ' Adicionado\n')

arquivo.close()
# w escrever
# r ler
# a escreve ao final do arquivo
