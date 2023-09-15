horaEntrada, minutoEntrada = input().split(':')
horaEntrada = int(horaEntrada)
minutoEntrada = int(minutoEntrada)

horaSaida, minutoSaida = input().split(':')
horaSaida = int(horaSaida)
minutoSaida = int(minutoSaida)

entradaEmMinutos = horaEntrada * 60 + minutoEntrada
saidaEmMinutos = horaSaida * 60 + minutoSaida

tempoNoEstacinamento = saidaEmMinutos - entradaEmMinutos

if tempoNoEstacinamento <= 15:
    print('Estacionamento Grátis')
elif tempoNoEstacinamento < 60:
    print('Valor à Pagar: R$ 2,00')
elif tempoNoEstacinamento < 120:
    print('Valor à Pagar: R$ 3,00')
elif tempoNoEstacinamento < 180:
    print('Valor à Pagar: R$ 4,00')
else:
    print('Valor à Pagar: R$ 5,00')