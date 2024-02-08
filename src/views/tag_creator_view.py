# Importa a classe HttpRequest do módulo http_request localizado no diretório src/views/http_types. Esta classe
# encapsula os dados de uma requisição HTTP.
from src.views.http_types.http_request import HttpRequest
# Importa a classe HttpResponse do módulo http_response localizado no diretório src/views/http_types. Esta classe
# encapsula os dados de uma resposta HTTP.
from src.views.http_types.http_response import HttpResponse
# Importa a classe TagCreatorController do módulo tag_creator_controller localizado no diretório src/controller.
# Esta classe é responsável por implementar as regras de negócio para a criação de tags.
from src.controller.tag_creator_controller import TagCreatorController

class TagCreatorView:
    """
       responsibility for interacting with HTTP
    """
    # Define o método validate_and_create, que recebe um objeto http_request do tipo HttpRequest como argumento e
    # retorna um objeto HttpResponse. Este método é responsável por validar a requisição recebida e criar uma resposta
    # HTTP.
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # Cria uma instância da classe TagCreatorController, que será usada para lidar com a lógica de negócios
        # relacionada à criação de tags.
        tag_creator_controller = TagCreatorController()
        # Obtém o corpo da requisição HTTP.
        body = http_request.body
        # Extrai o código do produto do corpo da requisição.
        product_code = body["product_code"]
        
        # lógica de regra de negócio
        # Chama o método create do controlador de criação de tags, passando o código do produto como argumento, para
        # obter uma resposta formatada.
        formatted_response = tag_creator_controller.create(product_code) 
        
        # Retorno HTTP
        # Retorna uma resposta HTTP com o status 200 (OK) e o corpo formatado da resposta do controlador de criação
        # de tags.
        return HttpResponse(status_code=200, body=formatted_response)

# Este código define uma classe chamada TagCreatorView, responsável por interagir com requisições HTTP.
    