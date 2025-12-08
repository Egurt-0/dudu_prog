import pytest
import functions
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    """
    Fixture que retorna um objeto de resposta mockado
    com status de code 200 e um
    corpo JSON especifico
   """
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {"message": "success"}
    return mock

def test_api_responde(mock_response):
    """
    Testa se a resposta mockada tem satatus 200
    e se o JSON esta correto
    """
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"message": "success"}
