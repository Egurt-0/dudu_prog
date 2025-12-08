import functions
import pytest
numeros = [1, 5, 7, 8, 9]



def add_numero(x, list):
    return list.append(x)


def teste_sub_and_len():
    assert functions.subtrair(3, 4) == -1
    assert functions.len_lista(numeros) == 5
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

    with pytest.raises(ValueError):
        functions.encontrar_valor('nao e um dicionario', 'a')