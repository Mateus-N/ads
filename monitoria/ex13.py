import phonenumbers
from phonenumbers import geocoder

def nome():
    nomeUserPerm = input('Gostaria que o remetente visse seu nome? Sim ou Não? ')
    if nomeUserPerm.lower().startswith('s') or nomeUserPerm.upper().startswith('S'):
        nomeUser = input('Insira seu nome: ')
        return nomeUser
    elif nomeUserPerm.lower().startswith('n') or nomeUserPerm.upper().startswith('N'):
        return None


def enviar_mensagem(numero, mensagem, nomeUser):
    print(f"Mensagem enviada para {numero}: {mensagem}")
    if nomeUser:
        print(f"Você recebeu uma mensagem de {nomeUser}, Numero: {telefone_ajustado.national_number}")
        print(mensagem)

while True:
    telefone = input('Digite o número de telefone (incluindo o código do país): ')

    try:
        telefone_ajustado = phonenumbers.parse(telefone)
        print(f'País: {telefone_ajustado.country_code} número: {telefone_ajustado.national_number}')

        local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
        print(f'Local: {local}')

        mensagem = input('Digite a mensagem que você deseja enviar: ')

        nomeUser = nome()
        enviar_mensagem(telefone, mensagem, nomeUser)
        break
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Número de telefone inválido. Por favor, tente novamente.")