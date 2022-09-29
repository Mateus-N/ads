# Ler os horarios de inicio e fim do teclado
horaI, minutoI, horaF, minutoF = str ( input ()).split()

# Armazenar os valores como inteiros
horaI = int (horaI)
minutoI = int (minutoI)
horaF = int (horaF)
minutoF = int (minutoF)

# Calcular o horario do inicio e final do jogo em minutos
totalMinutosI = minutoI + horaI * 60
totalMinutosF = minutoF + horaF * 60

# Verificar se o jogo terminou no dia seguinte
if totalMinutosF <= totalMinutosI :
  totalMinutosF += 24 * 60

# Calcular duração total do jogo em minutos
duracaoMinutos = totalMinutosF - totalMinutosI

# Calcular duração em horas
duracaoHoras = int ( duracaoMinutos // 60 )
duracaoMinutos -= duracaoHoras * 60

print (f'O JOGO DUROU {duracaoHoras} HORA(S) E {duracaoMinutos} MINUTO(S)')
