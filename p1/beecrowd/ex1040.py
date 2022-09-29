# Ler as quatro notas do aluno
nota1, nota2, nota3, nota4 = str ( input ()).split()

# Receber as notas com uma casa decimal
nota1 = round ( float (nota1), 1)
nota2 = round ( float (nota2), 1)
nota3 = round ( float (nota3), 1)
nota4 = round ( float (nota4), 1)

# Calcular a média com pesos 2, 3, 4 e 1
nota1 *= 2
nota2 *= 3
nota3 *= 4
nota4 *= 1

media = (nota1 + nota2 + nota3 + nota4) / 10

# Se média maior que 7
if media >= 7 :
  print (f'Media: {media:.1f}\nAluno aprovado.')

# Se média maior que 5
elif media < 5 :
  print (f'Media: {media:.1f}\nAluno reprovado.')

# Se média entre 5 e menor que 7
else :
  # Ler nota do exame
  exame = round ( float ( input ()), 1)
  # Calcular média final
  mediaFinal = (media + exame) / 2
  
  # Se média final maior ou igual a 5
  if mediaFinal >= 5 :
    print (f'''Media: {media:.1f}
Aluno em exame.
Nota do exame: {exame:.1f}
Aluno aprovado.
Media final: {mediaFinal:.1f}''')

  # Se média final menor que 5
  else :
    print (f'''Media: {media:.1f}
Aluno em exame.
Nota do exame: {exame:.1f}
Aluno reprovado.
Media final: {mediaFinal:.1f}''')
