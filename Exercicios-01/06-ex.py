"""Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

O volume do aquário em litros;
A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

Volume é dado por (comprimento * altura * largura) / 1000
A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

Utilize funções."""

comprimento = float(input("Digite o comprimento do aquário: "))
altura = float(input("Digite a altura do aquário: "))
largura = float(input("Digite a largura do aquário: "))
temperatura_desejada = float(input("Digite a temperatura desejada para o aquário: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente: "))

def volume(comprimento, altura = 1, largura = 1):
    return comprimento * altura * largura / 1000

def potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente 
    if temperatura_desejada > temperatura_ambiente 
    else temperatura_ambiente - temperatura_desejada)

def filtragem_por_hora(volume):
    return volume * 2, volume * 3

volume = volume(comprimento, altura, largura)

print(f"Volume: {volume}L")
print(f"Potência do termostato: {potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)}W")
print(f"Filtragem por hora: {filtragem_por_hora(volume)[0]}L {filtragem_por_hora(volume)[1]}L")
