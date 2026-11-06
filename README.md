# Caeser-Cipher-Implementation

Uma impementação simples sobre "Caeser Cipher ", trata-se uma técnica de criptografia em que a letra da mensagem é movida um número fixo de posições no alfabeto. Tem como objectivo de encriptar e desencriptar mensagens de forma simples.


Está incluido no projecto :

1. A criptografia do mensagem escolhida pelo utilizador
2. A desencriptação da mensagem
3. Uma chave primaria gerada aleatóriamente
4. Um menu de opções no terminal


Funcionalidade 

O programa permite :

Introduzir uma mensagem
Escolher entre : 
encrypt: Encriptar a mensagem
Decrypt: Desencriptar a mensagem
sair: encerrar o programa

NOTA: A key utilizada para encriptar e desencriptar é gerada automaticamente e pode variar de 1 a 25.


Funcionamento


A "Caesar Cipher" move cada letra do texto para outro ponto do alfabeto.

Se a chave for 3 :

*A vira D
*B vira E
*C vira F

Ex: A mensagem : "Hello" 
    Fica: "KHOOR"

Para desencriptar, faz-se o inverso.


Extrutura 

|__
   |__Main.py - Menu principal do programa
   |__Encrypt.py - Função para criptografar
   |__Decrypt.py - Função para desencriptar a mesnagem
   |__Hacking.py - 
   |__README.md - Documentaçao do Projecto


   
