#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

import random

def escolher_palavra():
    palavras = ["computador", "jogo", "elefante", "banana"]
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra secreta, uma letra de cada vez.")
    print(f"A palavra tem {len(palavra)} letras.")

    while tentativas_restantes > 0:
        print("\nPalavra:", mostrar_palavra_oculta(palavra, letras_corretas))
        print("Tentativas restantes:", tentativas_restantes)
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite uma letra válida.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            if len(letras_corretas) == len(set(palavra)):
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas_restantes -= 1

    if tentativas_restantes == 0:
        print("Você perdeu! A palavra era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()
