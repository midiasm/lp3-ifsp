#Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

def contar_vogais_consoantes(frase):
    vogais = 'aeiou'
    contador_vogais = 0
    contador_consoantes = 0

    for letra in frase:
        if letra.isalpha():
            if letra in vogais:
                contador_vogais += 1
            else:
                contador_consoantes += 1

    return contador_vogais, contador_consoantes

def main():
    frase = input("Digite uma frase em letras minúsculas: ")

    vogais, consoantes = contar_vogais_consoantes(frase)

    mensagem = f"Na frase {frase} temos: {vogais} vogais e {consoantes} consoantes."
    print(mensagem)

if __name__ == "__main__":
    main()
