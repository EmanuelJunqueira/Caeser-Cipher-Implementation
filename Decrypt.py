
LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(message, key):
    decrypted_message = [] 
    for char in message:
        if char.isalpha(): 

            posicao_original = LETRAS.find(char.upper())
            nova_posicao = (posicao_original - key) % 26 # a diferenca aqui é que substraimos

            decrypted_char = LETRAS[nova_posicao]
            decrypted_message.append(decrypted_char)

        else:
            decrypted_message.append(char) 
    return ''.join(decrypted_message)