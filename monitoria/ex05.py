hora_i, minuto_i = input().split(':')

hora_i = int(hora_i)
minuto_i = int(minuto_i)

hora_em_segundos = hora_i * 3600
minuto_em_segundos = minuto_i * 60
intervalo1 = ((8 * 60) + 15) * 1
intervalo2 = ((7 * 60) + 12) * 3
intervalo3 = ((8 * 60) + 15) * 1

segundos_partida = hora_em_segundos + minuto_em_segundos
tempo_gasto_atividade = intervalo1 + intervalo2 + intervalo3

segundos_chegada = segundos_partida + tempo_gasto_atividade

hora_chegada = segundos_chegada // 3600
minuto_chegada = (segundos_chegada % 3600) // 60
segundo_chegada = (segundos_chegada % 3600) % 60

print(f'{hora_chegada}:{minuto_chegada}:{segundo_chegada}')