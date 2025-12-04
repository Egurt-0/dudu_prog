import functions


def teste_soma():
    assert sum([1, 4, 5]) == 10



def teste_is_positive():
    assert functions.is_positive(5) is True
    assert functions.is_positive(-4) is False


def test_gmail():
    assert functions.valida_gmail("fulano@gmail.com") is True
    assert functions.valida_gmail("skibidi.com.br") is False