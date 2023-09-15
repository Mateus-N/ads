# Ler três valores inteiros
valorA, valorB, valorC = str ( input ()).split()

# Armazenar os valores como inteiros
valorA = int (valorA)
valorB = int (valorB)
valorC = int (valorC)

# Verificar se o valor A é o maior
if valorA >= valorB and valorA >= valorC:
  maior = valorA

  # Verificar o maior entre B e C
  if valorB >= valorC:
    medio = valorB
    menor = valorC
  else :
    medio = valorC
    menor = valorB

# Verificar se o valor B é o maior
elif valorB >= valorA and valorB >= valorC :
  maior = valorB

  # Verificar o maior entre A e C
  if valorA >= valorC :
    medio = valorA
    menor = valorC
  else :
    medio = valorC
    menor = valorA

# Se nenhuma das afirmações acima for verdade, C é o maior
else :
  maior = valorC

  # Verificar o maior entre A e B
  if valorA >= valorB :
    medio = valorA
    menor = valorB
  else :
    medio = valorB
    menor = valorA

print (f'''{menor}
{medio}
{maior}

{valorA}
{valorB}
{valorC}''')
