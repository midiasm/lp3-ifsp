"""Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora em Python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

IMC = peso / altura * altura

Classificação
----------------------------------
IMC           Classificação
-----------------------------------
< 18,5         Baixo peso
18,5 a 24,9     Peso normal
25,0 a 29,9     Excesso de peso
30,0 a 34,9     Obesidade de Classe 1
35,0 a 39,9     Obesidade de Classe 2
>= 40,00      Obesidade de Classe 3

Utilize funções."""

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

def imc(peso, altura):
    return peso / altura ** 2

def classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    if imc < 25.0:
        return "Peso normal"
    if imc < 30.0:
        return "Excesso de peso"
    if imc < 35.0:
        return "Obesidade de classe 1"
    if imc < 40.0:
        return "Obesidade de classe 2"
    else:
        return "Obesidade de classe 3"

def peso_a_perder(peso, altura):
    return peso - (24.9 * altura * altura)

imc = imc(peso, altura)
peso_a_perder = round(peso_a_perder(peso, altura))

print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao(imc)}")
mensagem = f"Você precisa perder ou ganhar peso? Seu IMC é: {imc}."
print(mensagem)