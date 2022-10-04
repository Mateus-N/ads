# Criar função para receber a nota do teclado
def receberNota():
  # Inicio repetição com True
  while True:

    # Ler nota do teclado
    nota = float ( input ('Digite a nota do aluno: '))
    # Verificar se a nota é válida
    if 0 <= nota <= 10:
      # Retornar nota e encerrar a função e o laço
      return nota
    # Caso contrário
    else:
      print('Nota inválida!')


# Declarar variáveis iniciadas em 0
somatorioDeNotas = 0
quantidadeNotas = 0

# Inicio repetição com True
while True:

  # Chamada da função receber notas e armazenar em nota
  nota = receberNota()
  # Adicionar o valor da nota ao somatorio
  somatorioDeNotas += nota
  # Adicionar um a quantidade de notas
  quantidadeNotas += 1

  # Verificar se há mais alguma nota
  continuar = input('Deseja digitar uma nova nota (S/N)? ').strip()

  # Caso não encerrar o laço
  if continuar[0] in 'Nn':
    break

# Calcular média
media = somatorioDeNotas / quantidadeNotas
# Imprimir média na tela
print(f'A média do aluno é {media:.1f}')
