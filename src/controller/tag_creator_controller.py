# Esta linha importa o tipo Dict do módulo typing, usado para especificar o tipo de retorno da função create e da
# função privada __format_response.
from typing import Dict
# Esta linha importa a classe BarcodeHandler do módulo barcode_handler localizado no diretório src.drivers.
from src.drivers.barcode_handler import BarcodeHandler

# Define uma classe chamada TagCreatorController que encapsula a funcionalidade para criar tags.
class TagCreatorController:
    """
        responsibility for implementing business rules
    """
    #  Define um método público chamado create que recebe um parâmetro product_code do tipo str e retorna um dicionário
    #  (Dict). Este método cria uma tag usando o código do produto fornecido e formata a resposta.
    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create__tag(product_code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response

    # Define um método privado chamado __create__tag que recebe um parâmetro product_code do tipo str e retorna um
    # caminho (str) para a tag criada. Este método instancia um BarcodeHandler e chama seu método create_barcode para
    # criar uma tag com base no código do produto.
    def __create__tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)

        return path_from_tag

    # Define um método privado chamado __format_response que recebe um parâmetro path_from_tag do tipo str e retorna um
    # dicionário (Dict) formatado. Este método formata a resposta com base no caminho fornecido para a tag.
    def __format_response(self, path_from_tag: str) -> Dict:
        return {
          "data": {
              "type": "Tag Image",
              "count": 1,
              "path": f'{path_from_tag}.png'
          }
        }
        