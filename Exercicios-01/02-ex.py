# Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

def media(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3

mensagem = f"A média aritmética dos números é: {media(numero1, numero2, numero3)}."
print(mensagem)