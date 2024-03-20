#Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.

identificador = str(input("Digite seu identificador: "))

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

valido = "válido" if identificador_valido(identificador) else "inválido"

mensagem = f"Seu identificador é: {valido}"
print(mensagem)