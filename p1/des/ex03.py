nota = float ( input ())

if nota > 10 or nota < 0 :
  print ('Nota inválida')
elif nota == 10 :
  print ('Conceito A+')
elif nota >= 9 :
  print ('Conceito A')
elif nota >= 8 :
  print ('Conceito B')
elif nota >= 7 :
  print ('Conceito C')
elif nota >= 6 :
  print ('Conceito D')
elif nota >= 5 :
  print ('Conceito E')
else :
  print ('Conceito F')
