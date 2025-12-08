import pytest
import functions

@pytest.fixture
def list_sample():
    return [10, 9, 8 ,6 , 7]

def teste_sum(list_sample):
    assert sum(list_sample) == 40

def test_len(list_sample):
    assert len(list_sample) == 5