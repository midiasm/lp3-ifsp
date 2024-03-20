# Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:
"""
Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
Compras iguais ou superiores a R$ 500,00 - 15% de desconto
"""

valor = float(input("Digite o valor da compra: "))

def calcular_desconto(valor):
    if valor < 10:
        return valor * 0.0
    elif valor >= 10 and valor < 100:
        return valor * 0.05
    elif valor >=100 and valor < 500:
        return valor * 0.1
    else:
        return valor * 0.15

percentual_desconto = calcular_desconto
valor_final = valor - calcular_desconto

print(f"Valor da compra: R$ {valor:.2f}")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}%")
print(f"Valor final com desconto: R$ {valor_final:.2f}")