# Tipos de dados

# Numérico

# int
idade = 10

# float
altura = 1.78

# Booleano
# True, False
verdade = True
mentira = False
ligado = True
frete_gratis = True

# str = string
# sequência de caracteres 
# literal de str
nome = "José"
nome = 'José'

# char
letra = "a"

#multilinhas
frase = """
Olá pessoal
teste
teste
"""

# interpolação de string
nome = "Sonia" 
idade = 23

# f-string
mensagem = f"Bom dia {nome}. Você tem {idade} anos"

nome = "Silvio Santos"
print(nome [2])
print(nome[-1])
print(nome[0:3])

# str são objetos
# métodos
print(nome.upper())
nome = nome.upper
print(nome)

# list
# lista de valores
# pode conter valores de tipos diferentes
# pode ser alterada (adicionar, remover)
habilidades = ['java', 'html', 'css']
print(habilidades[0])

habilidades[0] = 'javascipt'
habilidades.append('python')
print(habilidades)

#adicionar em uma posicão
habilidades.insert(0, 'kotlin')
print(habilidades)

#remove, sort, clear, copy...

for habilidade in habilidades:
    print(habilidade)

# tuple
# lista de valores 
# não pode alterar os valores

opcoes = ['sim', 'nao', 'talvez'] # lista
opcoes = ('sim', 'nao', 'talvez') # tuple 
raças_rpg = ('anao', 'humano', 'elfo')

print(opcoes[1])

# função que retorna estatisticas sobre as notas de um aluno
# media, menor nota, maior nota
# entrada: n1, n2, n3 ou notas (list)
# saida: media, menor nota, maior nota
def estatistica_nota(notas):
    media = sum(notas) / len(notas)
    menor =min(notas)
    maior = max(notas)
    return meida, menor, maior

notas = [10.0, 5.5, 3.2, 1.0]
estatistica = estatistica_nota(notas)
print(estatistica)
print(type(estatistica))

# desempacotamento de tuple
media, menor, maior = estatistica_nota(notas)
print(media, menor, maior)

# set
# conjunto de valores
# não permite valores duplicados
# não é inexado 
habilidades = ('java', 'python', 'css')
habilidades.add('java')
print(habilidades)

# dict 
# dicionario 
# palavras
# palavra = definição 
# chave => valor
# keu=y => value 
nome = 'Silvio Santos'
casado = True
idade = 90

pessoa = {
    'nome': 'Silvio Santos',
    'casado': True,
    'idade': 120
}

print(pessoa['nome'])
print(pessoa['casado'])
print(pessoa['idade'])

pessoa['rico'] = True
print(pessoa)

# None
# null
nulo = None


