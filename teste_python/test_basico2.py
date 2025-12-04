import functions
import pytest

numeros = [1, 5, 7, 8, 9]



def add_numero(x, list):
    return list.append(x)


def teste_sub_and_len():
    assert functions.subtrair(3, 4) == -1
    assert functions.len_lista(numeros) == 6 # ele retorna errado mesmo parecendo estar certo, pois depois da minha funcao add_numero, a lista tem 6 itens nao 5
    assert functions.len_lista([1, 4, 5]) == 3

def test_soma_list():
    assert functions.soma_list([1, 2, 3, 4]) == 10
    assert functions.soma_list([10.5, 4.5, 5]) == 20

    with pytest.raises(ValueError):
        functions.soma_list([1, 3, 'a'])

def test_encotrar_valor():
    dicionario = {'a': 1, 'b': 2, 'c': 4}
    assert functions.encontrar_valor(dicionario, 'a') == 1
    assert functions.encontrar_valor(dicionario, 'b') == 2
    assert functions.encontrar_valor(dicionario, 'c') == 4




print(functions.subtrair(69, 2))
print(functions.len_lista(numeros))
add_numero(67, numeros)
print(numeros)