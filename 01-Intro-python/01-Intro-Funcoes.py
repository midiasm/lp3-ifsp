# Função
# Modularizar o programa
# Reuso
# Manutenabilidade (correção de erros e novas funcionalidades)

# Declaração
def ola_mundo():
    print('Olá mundo')

# Chamada 
ola_mundo()

# Função sem retorno
def imprimir_mensagem(nome):
    print("Bom dia, (nome)")

# Função com retorno
def mensagem(nome):
    return f"Bom dia, {nome}"

imprimir_mensagem(Jose)

# Parâmetro e argumentos
def somar(numero1, numero2): 
    return numero1 + numero2

somar(10.0, 3.4)

# Escopo de variáeis
def media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total / 3

# Parâmetros com valor padrão
def mensagem(nome, mensagem):
    return f"{mensagem}, {nome}."

# Argumentos nomeados
print('Olá', '123', 'teste', sep='@', end="\n\n")
print('TESTE')

mensagem(nome='Lucas', mensagem='Boa tarde')
mensagem(mensagem='Boa tarde', nome='Lucas')

# Docstring
# Comentário de documentção

def somar(numero1, numero2):
    """
    Função que soma dois numeros

    parametro numero1: primeiro numero
    parametro numero2: segundo numero
    return: soma dois numeros
    """
    return numero1 + numero2

# Funções built-in
# print, type, len, sum, max, min, input
# ver no python3 interativo terminal

def media(*notas):
    return sum(notas) / len(notas)

print(media(10.0, 3.5, 7.5))
