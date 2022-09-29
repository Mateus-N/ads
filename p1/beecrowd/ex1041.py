# Ler dois valores do teclado
cordenadaX, cordenadaY = str ( input ()).split()

# Armazenar valores com uma casa decimal
cordenadaX = round ( float (cordenadaX), 1)
cordenadaY = round ( float (cordenadaY), 1)

# Verificar se está na origem
if cordenadaX == 0 and cordenadaY == 0 :
  print ('Origem')

# Verificar se está no eixo X
elif cordenadaY == 0 :
  print ('Eixo X')

# Verificar se está no eixo Y
elif cordenadaX == 0 :
  print ('Eixo Y')

else :

  # Verificar se está no Q1
  if cordenadaX > 0 and cordenadaY > 0 :
    print ('Q1')

  # Verificar se está no Q2
  elif cordenadaX < 0 and cordenadaY > 0 :
    print ('Q2')

  # Verificar se está no Q3
  elif cordenadaX < 0 and cordenadaY < 0 :
    print ('Q3')

  # Verificar se está no Q4
  elif cordenadaX > 0 and cordenadaY < 0 :
    print ('Q4')
