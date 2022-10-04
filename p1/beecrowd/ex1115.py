# Inicio de iteração utilizando True
while True:
  # Ler dois valores inteiros do teclado
  valor1, valor2 = map(int, str ( input ()).split())

  # Caso qualquer um dos valores for 0 encerrar a iteração
  if valor1 == 0 or valor2 == 0:
    break
  
  # Verificar se o ponto está no primeiro quadrante
  if valor1 > 0 and valor2 > 0:
    # Imprimir o nome do quadrante na tela
    print('primeiro')

  # Verificar se o ponto está no segundo quadrante
  elif valor1 < 0 and valor2 > 0:
    # Imprimir o nome do quadrante na tela
    print('segundo')
  
  # Verificar se o ponto está no terceiro quadrante
  elif valor1 < 0 and valor2 < 0:
    # Imprimir o nome do quadrante na tela
    print('terceiro')
  
  # Verificar se o ponto está no quarto quadrante
  elif valor1 > 0 and valor2 < 0:
    # Imprimir o nome do quadrante na tela
    print('quarto')
