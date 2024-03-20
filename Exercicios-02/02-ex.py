#Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

def main():
    while True:
        try:
            numero = int(input("Digite um número para exibir sua tabuada: "))
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    main()
