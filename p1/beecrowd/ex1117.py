# Inicio de iteração com True
while True:

  # Ler a primeira nota do teclado
  nota1 = float ( input ())

  # Caso a nota esteja entre 0 e 10
  if nota1 >= 0 and nota1 <= 10:
    # Interrompa o laço
    break

  # Caso contrário
  else:
    # Imprimir nota inválida na tela
    print('nota invalida')

# Inicio de iteração com True
while True:

  # Ler a segunda nota do teclado
  nota2 = float ( input ())

  # Caso a nota esteja entre 0 e 10
  if nota2 >= 0 and nota2 <= 10:
    # Interrompa o laço
    break

  # Caso contrário
  else:
    # Imprimir nota inválida na tela
    print('nota invalida')

# Calcular a média entre as notas
media = (nota1 + nota2) / 2

# Imprimir a média na tela com duas casas decimais
print(f'media = {media:.2f}')
