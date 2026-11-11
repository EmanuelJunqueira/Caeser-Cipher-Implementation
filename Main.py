import random

from Encrypt import encrypt
from Decrypt import decrypt
from Hacking import smart_brute_force

def main():
    key = None  # Inicializa a variável
    ultima_mensagem_cifrada = None  # Inicializa a variável 
    while True:

        message = input("Escreve a mensagem (ou 'sair' para fechar): ") 
        if message.strip().lower() == 'sair':  # strip remove espaços em branco no início e no fim da string
            print("Programa encerrado.")  
            break  

        action = input("Escolha o método (encrypt / decrypt / hack): ").strip().lower()  

        if action == 'encrypt':
            key = random.randint(1, 25)  # Gera uma chave aleatória entre 1 e 25
            encrypted_message = encrypt(message, key)  # Encripta a mensagem com a chave gerada

            ultima_mensagem_cifrada = encrypted_message  # Armazena a última mensagem encriptada

            print(f"\nMensagem Encriptada: {encrypted_message}")  
            print(f"(A chave aleatória gerada e guardada foi: {key})") 

        elif action == 'decrypt':
            if key is None:  # Verifica se nenhuma mensagem foi encriptada ainda
                print("\nErro: Nenhuma mensagem foi encriptada ainda!")

            elif message != ultima_mensagem_cifrada:  # Verifica se a mensagem inserida não é a última encriptada
                print("\nErro: Acesso negado! Essa não é a mensagem que foi encriptada.")
                
            else:
                decrypted_message = decrypt(message, key)  # Desencripta a mensagem com a chave armazenada
                print(f"\nMensagem Desencriptada: {decrypted_message}") 

                key = None  # Reseta a chave após desencriptação
                ultima_mensagem_cifrada = None  # Reseta a última mensagem encriptada

        elif action == 'hack':
            # Avisa o utilizador que o processo de ataque começou
            print("\n[!] Iniciando Hack de Força Bruta ...")
           
            # A função recebe o criptograma inserido (message) e devolve a chave provável e o texto descodificado
            discovered_shift, hacked_message = smart_brute_force(message)

            # Apresenta os resultados descobertos pelo algoritmo no ecrã
            print(f" Chave detetada pelo algoritmo: {discovered_shift}")
            print(f" Mensagem decifrada: {hacked_message}\n")

        else:
            print("\nAção inválida. Escolhe 'encrypt', 'decrypt' ou 'hack'.")  # Mensagem de erro para ações inválidas

if __name__ == "__main__": 
    main() 
