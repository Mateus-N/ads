# Ler data e hora de inicio da festa
_, diaI = str ( input ()).split()
horaI, minutoI, segundoI = str ( input ()).split(' : ')

# Armazenar valores como inteiros
diaI = int (diaI)
horaI = int (horaI)
minutoI = int (minutoI)
segundoI = int (segundoI)

# Ler data e hora do final da festa
_, diaF = str ( input ()).split()
horaF, minutoF, segundoF = str ( input ()).split(' : ')

# Armazenar valores como inteiros
diaF = int (diaF)
horaF = int (horaF)
minutoF = int (minutoF)
segundoF = int (segundoF)

# Armazenar o horario de inicio em segundos
inicioEmMinutos = horaI * 60 + minutoI
inicioEmSegundos = inicioEmMinutos * 60 + segundoI

# Armazenar o horario do final em segundos
finalEmMinutos = horaF * 60 + minutoF
finalEmSegundos = finalEmMinutos * 60 + segundoF

# Calcular o total de dias
totalDia = diaF - diaI

# Verificar se a festa terminou em dia subsequente mais cedo do que comecou
if finalEmSegundos < inicioEmSegundos :
  finalEmSegundos += 24 * 60 * 60
  totalDia -= 1

# Calcular duracao em segundos
totalSegundos = finalEmSegundos - inicioEmSegundos

# Calcular duração em minutos e remover esses minutos dos segundos
totalMinutos = totalSegundos // 60
totalSegundos -= totalMinutos * 60

# Calcular duração em horas e remover essas horas dos minutos
totalHoras = totalMinutos // 60
totalMinutos -= totalHoras * 60

# Imprimir as informações na tela
print (f'''{totalDia} dia(s)
{totalHoras} hora(s)
{totalMinutos} minuto(s)
{totalSegundos} segundo(s)''')
