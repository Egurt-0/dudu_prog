import pytest

def adicionar(x, y):
    return x + y

@pytest.mark.parametrize(
    "entrada_x, entrada_y, esperado",
    [
        (1, 2, 3),# sao 3 valores, os dois primeiros se somam e o terceiro e o resultado
        (0, 0, 0),
        (5, 6, 11),
        (4, 6, 10),
        (6, 7, 13)
    ]
)
def test_adicionar(entrada_x, entrada_y, esperado):
    resultado = adicionar(entrada_x, entrada_y)
    assert resultado == esperado