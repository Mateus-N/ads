# Declaração das variáveis e todas iniciando em 0
quantidadePositivos = 0
somaPositivos = 0
contador = 0

# Inicio da iteração que irá continuar
# enquanto o contador for menor que 6
while contador < 6:

  # Leitura de um valor númerico do teclado
  valor = float ( input ())
  # Incremento do contador a cada iteração
  contador += 1
  # Verificar se o valor digitado é positivo
  if valor >= 0:
    # Caso sim é adicionado 1 a quantidade
    # de valores positivos digitados
    quantidadePositivos += 1
    # E valor é somado à variável somaPositivos
    somaPositivos += valor

# Calculo da média de valores positivos
media = somaPositivos / quantidadePositivos

# Imprimir na tela a quantodade de valores positivos
# e sua média com uma casa decimal
print(f'''{quantidadePositivos} valores positivos
{media:.1f}''')
