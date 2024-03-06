# if, if/else, if/elif/else, ternario, match

#if
#if condicao
# codigo do if
# codigo do if
#codigo

idade = 20
if idade >= 18:
    print('maior')

#if/else

if idade >= 18:
    print('maior')
else: 
    print('menor')

#elif
#crianca 0 a 12, adolescente 13 a 17, adulto 18 a 59, idoso 60+
idade = 30
if idade <= 12:
    print('crianca')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')

# evitar alinhamennto de ifs
email = ''
senha = ''

if email == 'admin@email.com':
    if senha == '123admin':
        print('liberado')
else:
    print('email ou senha incorretos')

if email == 'admin123@email.com' and senha == '123admin':
    print('liberado')
else:
    print('email ou senha incorretos')

# entrada numero 1, 2, 3 ...7
# saida dia: domingo, segunda, terca ...sabado

dia = 4

if dia == 1:
    print('domingo')
elif dia == 2:
    print('segunda')
elif dia == 3:
    print('terça')
else:
    print('outro')

dias = {
    1:('domingo'),
    2:('segunda'),
    3:('terca'),
    4:('quarta'),
    5:('quinta'),
    6:('sexta'),
    7:('sabado')
}

if dia in dias:
    print({dia})
else:
    print('dia invalido')

# ternario
media = 6.0

if media >= 6.0:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

situacao = 'aprovado' if media >= 6.0 else 'reprovado'

# match

match dia:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3:
        print('terca')
    case 4:
        print('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sabado')
    case _:
        print('invalido')

# dia util 2, 3, 4, 5, 6
# final de semana 7, 1

# if dia == 2: or dia == 4 or dia == 5

match dia:
    case 2 | 3 | 4 | 5 | 6:
        print('dia util')
    case 1 | 7:
        print('final de semana')
    case _:
        print('dia invalido')

