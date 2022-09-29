# Definição da função que irá contar a quantidades de cédulas
def contadorCedulas (valor, cedula, quantidade = 0) :

  # Caso o valor for maior que o valor da cédula é adicionada uma cedula a contagem
  if valor >= cedula :
    
    valor -= cedula
    quantidade += 1

    # Recursividade para adicionar mais uma quantidade a cédula
    return contadorCedulas (valor, cedula, quantidade)

  # Fim da função
  return quantidade


# Definição da função que irá trocar o valor das cédulas e fazer o print das quantidades na tela
def cedulas (valor , cedula = 100 ) :

  # Execução da função para contar a quantidade de cédulas
  quantidadeCedulas = contadorCedulas (valor, cedula)

  # Calculo do valor após a função anterior
  valor -= quantidadeCedulas * cedula

  # Imprimir na tela a quantidade daquela cédula
  print (f'{quantidadeCedulas} nota(s) de R$ {cedula},00')

  # Mudança da cédula de 100 para 50
  if cedula == 100 :
    return cedulas (valor, 50)

  # Mudança da cédula de 50 para 20
  elif cedula == 50 :
    return cedulas (valor, 20)

  # Mudança da cédula de 20 para 10
  elif cedula == 20 :
    return cedulas (valor, 10)

  # Mudança da cédula de 10 para 5
  elif cedula == 10 :
    return cedulas (valor, 5)

  # Mudança da cédula de 5 para 2
  elif cedula == 5 :
    return cedulas (valor, 2)

 # Mudança da cédula de 2 para 1
  elif cedula == 2 :
    return cedulas (valor, 1)

  # Fim da função
  else :
    return None


# Ler valor do teclado
valor = int ( input ())

# Imprimir valor na tela
print (valor)

# Execução da função
cedulas (valor)
