import pytest

def funcao_unidade(x):
    """Funcao de exemplos para testes unitarios"""
    return x * 2

def funcao_integracao(x):
    """funcao de exemplo para teste de integracao"""
    return x + 10

# teste unitario
@pytest.mark.unit
def teste_funcao_unidade():
    assert funcao_unidade(20) == 40
    assert funcao_unidade(0) == 0
    assert funcao_unidade(-1) == -2


@pytest.mark.integracao
def teste_funcao_integracao():
    assert funcao_integracao(20) == 30
    assert funcao_integracao(0) == 10
    assert funcao_integracao(9) == 19


@pytest.mark.slow # para executar use pytest -m slow
def teste_funcao_lenta():
    import time
    time.sleep(3)
    assert True


@pytest.mark.unit
@pytest.mark.integracao
def teste_funcao_combinada():
    assert funcao_integracao(2) == 12
    assert funcao_unidade(4) == 8
    


