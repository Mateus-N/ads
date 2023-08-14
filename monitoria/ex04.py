def ehBissexto(ano):
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    return 'bissexto'
  return 'Não bissexto'


while True:
  for i in range(5):
    ano = int ( input ())
    print(ehBissexto(ano))
  
  resposta = input ('Voce esta ai? ')
  if resposta.lower() != 'sim':
    break
