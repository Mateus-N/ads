# Declaração das variáveis, todas iniciando em 0
contador = 0
dentroDoIntervalo = 0
foraDoIntervalo = 0

# Ler um valor inteiro do teclado
repeticoes = int ( input ())

# Inicio da iteração que irá se repetir enquanto
# o contador for menor que a variável repetições
while contador < repeticoes:

  # Ler um valor inteiro do teclado
  valor = int ( input ())
  # Incrementar o contador em 1
  contador += 1
  # Verificar se o valor digitado está
  # dentro do intervao [10,20]
  if valor >= 10 and valor <= 20:
    # Caso sim a variável dentroDoIntervalo
    # é incrementada em 1
    dentroDoIntervalo += 1
  else:
    # Caso contrário a variável foraDoIntervalo
    # é incrementada em 1
    foraDoIntervalo += 1

# Imprimir na tela as váriaveis
# dentroDoIntervalo e foraDoIntervalo
print(f'''{dentroDoIntervalo} in
{foraDoIntervalo} out''')
