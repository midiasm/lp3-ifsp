# Escreva um programa em Python que solicita ao usuário um número inteiro e apresenta seu antecessor e sucessor.

numero = int(input("Digite um numero: "))

def antecessor(numero):
    return numero - 1

def sucessor(numero):
    return numero + 1

mensagem = f"O antecessor é: {antecessor(numero)}."
print(mensagem)
mensagem = f"O sucessor é: {sucessor(numero)}."
print(mensagem)