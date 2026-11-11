
LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, key):
    encrypted_message = [] # isto representa uma lista vazia 
    for char in message:
        if char.upper() in LETRAS: #
          
            posicao_original = LETRAS.find(char.upper()) # aqui é transformado a letra original em Maiuscula

            # utiliza o operador módulo (%) para garantir que o índice fique dentro do intervalo de 0 a 25
            nova_posicao = (posicao_original + key) % 26 


            encrypted_char = LETRAS[nova_posicao]
            encrypted_message.append(encrypted_char)
            
        else:
            encrypted_message.append(char) # se o caractere não for uma letra, ele é adicionado à lista sem alterações
    return ''.join(encrypted_message)
