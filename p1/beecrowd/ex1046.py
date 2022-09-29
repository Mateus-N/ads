# Ler horario do inicio e do final
inicio, final = str ( input ()).split()

# Armazenar os valores como inteiros
inicio = int (inicio)
final = int (final)

# Verificar se o jogo terminou no dia seguite
if final <= inicio :
  final += 24

# Armazenar a duração do jogo
duracao = final - inicio

# Imprimir duranção na tela
print (f'O JOGO DUROU {duracao} HORA(S)')
