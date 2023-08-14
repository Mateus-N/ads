frase = input()

letrasJuntas = 0
for i in range(1, len(frase)):
    if frase[i] == frase[i - 1]:
        letrasJuntas += 1

if letrasJuntas == 0:
    print('Não há palavras com letras repetidas')
else:
    print(f'Na frase há {letrasJuntas} palavras com letras repetidas')