# Funcao que ira traduzir a frase
def traduzirFrase(frase):
    # Inicio da traducao vazia
    traducao = ''
    # Laco para percorrer a frase
    for chave in frase:
        # Buscar a letra no dicionario
        letra = morse[chave]
        # Concatena a letra com a traducao
        traducao += letra
    
    # Retorna a traducao
    return traducao


morse = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '/': ' '
}

# Receber morse do teclado
entrada = input().split(' ')

# Tentar traduzir a frase
try:
    frase = traduzirFrase(entrada)
    # Imprimir a traducao
    print(frase)
except:
    print('Erro na entrada.')
