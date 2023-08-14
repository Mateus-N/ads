def contadorCedulas (valor, cedula, quantidade = 0) :
  if valor >= cedula :
    valor -= cedula
    quantidade += 1
    return contadorCedulas (valor, cedula, quantidade)
  return quantidade

def cedulas (valor , cedula = 100 ) :
    quantidadeCedulas = contadorCedulas (valor, cedula)
    valor -= quantidadeCedulas * cedula
    print (f'{quantidadeCedulas} nota(s) de R$ {cedula},00')
    if cedula == 100 :
        return cedulas (valor, 50)
    elif cedula == 50 :
        return cedulas (valor, 20)
    elif cedula == 20 :
        return cedulas (valor, 10)
    elif cedula == 10 :
        return cedulas (valor, 5)
    elif cedula == 5 :
        return cedulas (valor, 2)
    elif cedula == 2 :
        return cedulas (valor, 1)
    else :
        return None

valor = int ( input ())
print (valor)
cedulas (valor)