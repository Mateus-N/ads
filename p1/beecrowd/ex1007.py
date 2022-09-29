# Ler quatro valores inteiros
primeiroValor = int ( input ())
segundoValor = int ( input ())
terceiroValor = int ( input ())
quartoValor = int ( input ())

# Armazenar o produto
# do primeiro pelo segundo
primeiroProduto = primeiroValor * segundoValor
# do terceiro pelo quarto
segundoProduto = terceiroValor * quartoValor

# Armazenar a diferença entre os produtos
diferenca = primeiroProduto - segundoProduto

# Mostrar diferença na tela
print (f'DIFERENCA = {diferenca}')
