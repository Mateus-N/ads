# Ler três valores
valores = str ( input ()).split()

# Armazenar os valores em variáveis simples
# com o tipo inteiro
valorA = int ( valores[0])
valorB = int ( valores[1])
valorC = int ( valores[2])

# Condicionais para verificar o maior valor
# caso A for o maior valor
if valorA >= valorB and valorA >= valorC :

  # Imprimir na tela que A é o maior valor
  print (f'{valorA} eh o maior')

# caso B for o maior valor
elif valorB >= valorA and valorB >= valorC :

  # Imprimir na tela que B é o maior valor
  print (f'{valorB} eh o maior')

# caso C for o maior valor
else :

  # Imprimir na tela que C é o maior valor
  print (f'{valorC} eh o maior')
