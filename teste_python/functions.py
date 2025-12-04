def subtrair(x, y):
    return x - y


def len_lista(list):
    return len(list)


def is_positive(x):
    return x > 0


def valida_gmail(gmail):
    return '@' in gmail and '.' in gmail


def soma_list(valores):
    """soma todos os valores em uma lista """
    if not all(isinstance(i, (int, float)) for i in valores):
        raise ValueError("Todos os itens na lista devem ser numeros")
    return sum(valores)


def encontrar_valor(dicionario, chave):
    """Retorna valor assosicado a uma chave e um dicionario"""
    if not isinstance(dicionario, dict):
        raise ValueError("O primeiro argumento deve ser um dicionario")
    return dicionario.get(chave, None)

