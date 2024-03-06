# Operadores aritméticos
# +, -, /, *, %

nota1 = 10
nota2 = 3
media = (nota1 + nota2) / 2

# potencia
numero = 2 ** 3 # elevado ao cubo
numero = 10 ** 2 # elevado ao quadrado

# lógicos
# and, or, not
# acesso liberado = nao bloqueado, idade > 18, horario comercial

bloqueado = False
idade  = 21
hora_atual = 10

horario_comercial = hora_atual >= 8 and hora_atual <= 18
maior_idade = idade >= 18

if not bloqueado and idade > 18 and hora_atual >= 8 and hora_atual <=18:
    print('liberado')
else:
    print('nao liberado')

# operadores de comparação
# >, <, >=, <=, ==, =!
numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) # True

# operador is
print(numeros is numeros2) # False

numeros3 = [1, 2]
numeros4 = numeros 3
print(numeros 3 is numeros4) # True
print(numeros 3 is not numeros4) # True

# in (bool)
print('a' in 'python') # False
prontuarios = ['Sp3090621', 'Sp3060624', 'Sp3030942']
prontuario = 'Sp3090621'
print (prontuario in prontuarios) # True

# sim, nao, talvz
opcao = ''

if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
    print('opcao valida')
else:
    print('opcao invalida')

opcoes == ('sim', 'nao', 'talvez')
if opcao in opcoes: 
    print ('opcao valida')
else:
    print('opcao invalida')





