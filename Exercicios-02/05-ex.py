#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

def verificar_palindromo(texto):
    return texto == texto[::-1]

def main():
    palavra_frase = input("Digite uma palavra ou frase: ")
    if verificar_palindromo(palavra_frase):
        print(f"A palavra/frase '{palavra_frase}' é um palíndromo.")
    else:
        print(f"A palavra/frase '{palavra_frase}' não é um palíndromo.")

if __name__ == "__main__":
    main()
