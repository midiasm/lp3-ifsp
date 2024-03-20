#Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

def converter_nota(pontuacao):
    if pontuacao >= 80:
        return "A"
    elif pontuacao >= 60 and pontuacao < 80:
        return "B"
    elif pontuacao >= 40 and pontuacao < 60:
        return "C"
    else:
        return "D"

def main():
    while True:
        try:
            pontuacao = float(input("Digite a pontuação (0 a 100): "))
            if pontuacao < 0 or pontuacao > 100:
                print("Por favor, digite uma pontuação válida entre 0 e 100.")
                continue
            break
        except ValueError:
            print("Por favor, digite uma pontuação válida.")

    nota = converter_nota(pontuacao)
    print(f"A nota correspondente à pontuação {pontuacao} é: {nota}")

if __name__ == "__main__":
    main()
