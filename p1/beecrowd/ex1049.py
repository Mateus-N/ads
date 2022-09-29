# Ler informações do animal do teclado
formacao = str ( input ()).lower()
divisao = str ( input ()).lower()
alimento = str ( input ()).lower()

# Verificar se o animal é vertebrado
if formacao == 'vertebrado' :  
  # Verificar se o animal é ave
  if divisao == 'ave' :
    # Verificar se o animal é carnivoro
    if alimento == 'carnivoro' :
      animal = 'aguia'
    
    # Verificar se o animal é onivoro
    elif alimento == 'onivoro' :
      animal = 'pomba'
  
  # Verificar se o animal é mamifero
  elif divisao == 'mamifero' :
    # Verificar se o aniimal é onivoro
    if alimento == 'onivoro' :
      animal = 'homem'
    
    # Verificar se o animal é herbivoro
    elif alimento == 'herbivoro' :
      animal = 'vaca'

# Verificar se o animal é invertebrado
elif formacao == 'invertebrado' :
  # Verificar se é um inseto
  if divisao == 'inseto' :
    # Verificar se o animal é hematofago
    if alimento == 'hematofago' :
      animal = 'pulga'

    # Verificar se o animal é herbivoro
    elif alimento == 'herbivoro' :
      animal = 'lagarta'
    
  # Verificar se o animal é anelideo
  elif divisao == 'anelideo' :
    # Verificar se o animal é hematofago
    if alimento == 'hematofago' :
      animal = 'sanguessuga'

    #Verificar se o animal é onivoro
    elif alimento == 'onivoro' :
      animal = 'minhoca'

# Imprimir o nome do animal na tela
print (animal)
