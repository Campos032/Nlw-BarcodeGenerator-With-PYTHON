# Importa a função patch do módulo unittest.mock, que será usada para simular o comportamento da função create_barcode.
from unittest.mock import patch
# Importa a classe BarcodeHandler, que será mockada no teste.
from src.drivers.barcode_handler import BarcodeHandler
# Importa a classe TagCreatorController, que será testada.
from .tag_creator_controller import TagCreatorController

# Decora a função de teste com o patch, que irá substituir a função create_barcode da classe BarcodeHandler por um
# objeto mock durante a execução do teste.
@patch.object(BarcodeHandler, "create_barcode")
# Define a função de teste test_create, que recebe um parâmetro mock_create_barcode, que representa o objeto mock
# criado para substituir create_barcode.
def test_create(mock_create_barcode):
    # Define um valor de retorno esperado para a função create_barcode.
    mock_value = "image_path"
    # Configura o comportamento do objeto mock, especificando que ele deve retornar mock_value quando chamado.
    mock_create_barcode.return_value = mock_value
    # Cria uma instância da classe TagCreatorController.
    tag_creator_controler = TagCreatorController()
    
    # Chama o método create da instância tag_creator_controler com mock_value como argumento e armazena o resultado na
    # variável result.
    result = tag_creator_controler.create(mock_value)
    
    # Verifica se o resultado retornado é um dicionário.
    assert isinstance(result, dict)
    # Verifica se a chave "data" está presente no dicionário retornado.
    assert "data" in result
    # Verifica se a chave "type" está presente no dicionário aninhado sob a chave "data".
    assert "type" in result["data"]
    # Verifica se a chave "count" está presente no dicionário aninhado sob a chave "data".
    assert "count" in result["data"]
    # Verifica se a chave "path" está presente no dicionário aninhado sob a chave "data".
    assert "path" in result["data"]
    
    # Verifica se o valor associado à chave "type" dentro do dicionário aninhado sob a chave "data" é igual a
    # "Tag Image".
    assert result["data"]["type"] == "Tag Image"
    # Verifica se o valor associado à chave "count" dentro do dicionário aninhado sob a chave "data" é igual a 1.
    assert result["data"]["count"] == 1
    # Verifica se o valor associado à chave "path" dentro do dicionário aninhado sob a chave "data" é igual a
    # f"{mock_value}.png", ou seja, se é igual à concatenação de mock_value com a string ".png".
    assert result["data"]["path"] == f"{mock_value}.png"
