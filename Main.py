import random

from Encrypt import encrypt
from Decrypt import decrypt

def main():
    key = None
    ultima_mensagem_cifrada = None
    while True:

        message = input("Escreve a mensagem (ou 'sair' para fechar): ")
        if message.strip().lower() == 'sair':
            print("Programa encerrado.")
            break


        action = input("Escolha o método (encrypt / decrypt): ").strip().lower()

        if action == 'encrypt':
            key = random.randint(1, 25)    
            encrypted_message = encrypt(message, key)

            ultima_mensagem_cifrada = encrypted_message

            print(f"\nMensagem Encriptada: {encrypted_message}")
            print(f"(A chave aleatória gerada e guardada foi: {key})")

        elif action == 'decrypt':
            if key is None:
                print("\nErro: Nenhuma mensagem foi encriptada ainda!")

            elif message != ultima_mensagem_cifrada: 
                print("\nErro: Acesso negado! Essa não é a mensagem que foi encriptada.")
                
            else:
                decrypted_message = decrypt(message, key)
                print(f"\nMensagem Desencriptada: {decrypted_message}")

                key = None
                ultima_mensagem_cifrada = None
        else:
            print("\nAção inválida. Escolhe 'encrypt' ou 'decrypt'.")

if __name__ == "__main__":
    main()