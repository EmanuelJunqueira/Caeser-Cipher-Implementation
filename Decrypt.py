import string
import random

def decrypt(message, key):
    decrypted_message = []
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)