

def main():
    key = None
    while True:
        message = input("Digite a mensagem: ")
        action = input("Escolha o método (encrypt, decrypt ou sair): ").strip().lower()

        if action == 'sair':
            print("Programa encerrado.")
            break
        elif action == 'encrypt':
            if key is None:
                key = random.randint(1, 25)
            encrypted_message = encrypt(message, key)
            print(f"Mensagem criptografada: {encrypted_message}")
        elif action == 'decrypt':
            if key is not None:
                decrypted_message = decrypt(message, key)
                print(f"Mensagem descriptografada: {decrypted_message}")
            else:
                print("Erro: Nenhuma chave foi gerada ainda. Por favor, ecrypt primeiro.")
        else:
            print("Ação inválida. Escolha entre 'encrypt', 'decrypt' ou 'sair'.")

if __name__ == "__main__":
    main()