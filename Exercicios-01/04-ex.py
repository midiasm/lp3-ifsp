"""Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.

Exemplos válidos:

    BR0001X
    BR1236X
    BR9999X

Exemplos inválidos:

    br0001X
    BR126X
    BR99999X
    BR9999Y
    
Crie uma função em Python que implementa essa verificação
"""

def identificador_valido(identificador: str):

    if len(identificador) != 7:
        return False
    if not f"{identificador[0]}{identificador[1]}" == "BR":
        return False
    if not int(identificador[2:6]):
        return False 
    if not identificador[len(identificador) - 1] == "X":
        return False
    
    return True