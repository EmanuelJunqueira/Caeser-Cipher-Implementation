from Decrypt import decrypt

#Lista de Frequencias de letras em ingles (em percentagem)

ENGLISH_FREQ = {

    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974,
    'z': 0.074,
}

def score_text(text):
    # Quanto menor a nota, mais o texto se aproxima das frequências do inglês.
    text_lower = text.lower()
    # Conta quantas letras reais existem no texto
    letter_count = sum(1 for character in text_lower if character in ENGLISH_FREQ)

    # Se a mensagem for só unmeros ou símbolos , a nota é infinita ou seja apresneta um erro
    if letter_count == 0:
        return float('inf')

    #Dicionario que vai guardar quantas vezes cada letra aparece na mensagem
    observed = {}

    for character in text_lower:
        if character in ENGLISH_FREQ:
            observed[character] = observed.get(character, 0) + 1 #conta +1 cada vez que aparece uma letra

    # Distância de qui-quadrado entre frequências observadas e esperadas.
    chi_squared = 0.0

    for letter, expected_pct in ENGLISH_FREQ.items():
        expected_count = (expected_pct / 100.0) * letter_count #Quantidade esperada
        actual_count = observed.get(letter, 0)                 # Quantidade real


        #Se for muito diferente do esperado, a variavel (chi_squared) aumenta muito ou seja pior nota
        if expected_count > 0:
            chi_squared += ((actual_count - expected_count) ** 2) / expected_count

    return chi_squared


def smart_brute_force(ciphertext):
    # Testa as 25 chaves possíveis e escolhe a mensagem com a menor nota.
    best_shift = 0
    best_score = float('inf') #começa com a pior nota possivel (infinito)
    best_text = ciphertext

    for shift in range(1, 26):
        #Desencripta a menssgame com a chave atual e calcula a nota
        decrypted = decrypt(ciphertext, shift)

        score = score_text(decrypted)

        #Se a nota for menor (ou seja melhor) 
        if score < best_score:
            best_score = score #Atualiza a melhor nota
            best_shift = shift #Guarda a chave que deu esta nota
            best_text = decrypted # Guarda o texto que faz sentido

    return best_shift, best_text
