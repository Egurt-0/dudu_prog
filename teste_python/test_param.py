import pytest
import math
def calcular_area(base, altura):
    return base * altura


pytest.fixture
def dados_teste():
    """
    Fixture que fornece diferente conjuntos de dados para testar a funcao de calculo
    de area
    """

    return [
        {"base": 7, "altura": 7, "esperado": 49},
        {"base": 14, "altura": 27, "esperado": 2637},
        {"base": 2, "altura": 14, "esperado": 28},
        {"base": 4, "altura": 7, "esperado": 28},
        {"base": 9, "altura": 9, "esperado": 81},
    ]




@pytest.mark.parametrize("dados", [
    {"base": 7, "altura": 7, "esperado": 49},
        {"base": 14, "altura": 27, "esperado": 378},
        {"base": 2, "altura": 14, "esperado": 28},
        {"base": 4, "altura": 7, "esperado": 28},
        {"base": 9, "altura": 9, "esperado": 81},   
])

def test_calcular_area(dados):
    base = dados['base']
    altura = dados['altura']
    esperado = dados['esperado']
    assert base * altura == esperado





raio = 34
comprimento = 68
area_do_circulo = math.pi*pow(raio, 2)# esse pow e o expoente, entao (numero, expoente)
print(area_do_circulo)

