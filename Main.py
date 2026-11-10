import random

from Encrypt import encrypt
from Decrypt import decrypt
from Hacking import smart_brute_force

def main():
    key = None
    ultima_mensagem_cifrada = None
    while True:

        message = input("Escreve a mensagem (ou 'sair' para fechar): ")
        if message.strip().lower() == 'sair':
            print("Programa encerrado.")
            break


        action = input("Escolha o método (encrypt / decrypt / hack): ").strip().lower()

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


        elif action == 'hack':
            # Avisa o utilizador que o processo de ataque começou
            print("\n[!] Iniciando Hack de Força Bruta ...")
           
            # A função recebe o criptograma inserido (message) e devolve a chave provável e o texto descodificado
            discovered_shift, hacked_message = smart_brute_force(message)


            # Apresenta os resultados descobertos pelo algoritmo no ecrã

            print(f" Chave detetada pelo algoritmo: {discovered_shift}")
            print(f" Mensagem decifrada: {hacked_message}\n")

        else:
            print("\nAção inválida. Escolhe 'encrypt', 'decrypt' ou 'hack'.")

if __name__ == "__main__":
    main()
