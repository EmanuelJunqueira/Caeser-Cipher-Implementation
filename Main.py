import random

from Encrypt import encrypt
from Decrypt import decrypt

def main():
    key = None
    while True:

        message = input("Escreve a mensagem (ou 'sair' para fechar): ")
        if message.strip().lower() == 'sair':
            print("Programa encerrado.")
            break


        action = input("Escolha o método (encrypt / decrypt): ").strip().lower()

        if action == 'encrypt':
            key = random.randint(1, 25)
                
            encrypted_message = encrypt(message, key)
            print(f"\nMensagem Encriptada: {encrypted_message}")
            print(f"(A chave aleatória gerada e guardada foi: {key})")

        elif action == 'decrypt':
            if key is None:
                decrypted_message = decrypt(message, key)
                print(f"Mensagem descriptografada: {decrypted_message}")
            else:
                print("Erro: Nenhuma chave foi gerada ainda. Por favor, ecrypt primeiro.")
        else:
            print("Ação inválida. Escolha entre 'encrypt', 'decrypt' ou 'sair'.")

if __name__ == "__main__":
    main()