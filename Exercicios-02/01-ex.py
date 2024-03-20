#Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

import random

def jogo_de_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    
    tentativas = 0
    while True:
        palpite = int(input("Adivinhe o número entre 1 e 100: "))
        
        if palpite == numero_aleatorio:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas + 1} tentativas.")
            break
        elif palpite < numero_aleatorio:
            print("O seu palpite está baixo. Tente novamente.")
        else:
            print("O seu palpite está alto. Tente novamente.")
        
        tentativas += 1

jogo_de_adivinhacao()
