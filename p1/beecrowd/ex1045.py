# Ler três valores do teclado
valor1, valor2, valor3 = str ( input ()).split()

# Armazenar os valores como float com duas casas decimais
valor1 = round ( float (valor1), 2)
valor2 = round ( float (valor2), 2)
valor3 = round ( float (valor3), 2)

# Assumir que os valores foram digitados do maior para o menor
ladoA = valor1
ladoB = valor2
ladoC = valor3

# Caso não foram realizar a subtituição
if valor3 > valor2 :
  ladoB = valor3
  ladoC = valor2

# Verificar se o valor 2 é o maior
if valor2 >= valor1 and valor2 >= valor3 :
  ladoA = valor2

  # Verificar o maior entre valor 2 e valor 3
  if valor1 >= valor3 :
    ladoB = valor1
    ladoC = valor3
  else :
    ladoB = valor3
    ladoC = valor1

# Se nenhuma das afirmações acima for verdade, valor 3 é o maior
else :
  ladoA = valor3

  # Verificar o maior entre valor 1 e valor 2
  if valor1 >= valor2 :
    ladoB = valor1
    ladoC = valor2
  else :
    ladoB = valor2
    ladoC = valor1

# Verificar se os lados juntos formam um triangulo
if ladoA >= ladoB + ladoC :
  print ('NAO FORMA TRIANGULO')

else :
  # Verificar se é um TRIANGULO RETANGULO
  if ladoA ** 2 == ladoB ** 2 + ladoC ** 2 :
    print ('TRIANGULO RETANGULO')

  # Verificar se é um TRIANGULO OBTUSANGULO
  elif ladoA ** 2 > ladoB ** 2 + ladoC ** 2 :
    print ('TRIANGULO OBTUSANGULO')

  # Verificar se é um TRIANGULO ACUTANGULO
  elif ladoA ** 2 < ladoB ** 2 + ladoC ** 2 :
    print ('TRIANGULO ACUTANGULO')
  
  # Verificar se é um TRIANGULO EQUILATERO
  if ladoA == ladoB == ladoC :
    print ('TRIANGULO EQUILATERO')
  
  # Verificar se é um TRIANGULO ISOSCELES
  elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC :
    print ('TRIANGULO ISOSCELES')
