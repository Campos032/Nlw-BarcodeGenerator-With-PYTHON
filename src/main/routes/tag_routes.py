# Importa as funções e classes necessárias do framework Flask para criar rotas HTTP, acessar a requisição HTTP recebida
# e serializar a resposta HTTP.
from flask import Blueprint, request, jsonify
# Importa a classe HttpRequest do módulo http_request localizado no diretório src/views/http_types. Esta classe é
# responsável por encapsular os dados da requisição HTTP.
from src.views.http_types.http_request import HttpRequest
# Importa a classe TagCreatorView do módulo tag_creator_view localizado no diretório src/views. Esta classe é
# responsável por criar e validar tags.
from src.views.tag_creator_view import TagCreatorView

# Cria um objeto Blueprint chamado tag_routes_bp para definir rotas relacionadas a tags.
tag_routes_bp = Blueprint('tags_routes', __name__)

# Define um decorador para a função abaixo que especifica que essa função será chamada quando uma requisição HTTP POST
# for feita para a rota /create_tag.
@tag_routes_bp.route('/create_tag', methods=['POST'])
# Define a função create_tagg, que será chamada quando uma requisição POST for feita para a rota /create_tag.
def create_tagg():
    # Cria uma instância da classe TagCreatorView, que será usada para manipular a criação de tags.
    tag_creator_view = TagCreatorView()
    # Cria uma instância da classe HttpRequest, passando o corpo da requisição HTTP recebida como argumento. Isso
    # encapsula os dados da requisição em um objeto HttpRequest.
    http_request = HttpRequest(body=request.json)
    # Chama o método validate_and_create da instância de TagCreatorView, passando o objeto http_request como argumento.
    # Este método valida os dados da requisição e cria a tag.
    response = tag_creator_view.validate_and_create(http_request)
    # Retorna a resposta da requisição HTTP, serializando o corpo da resposta para o formato JSON e retornando o código
    # de status HTTP correspondente.
    return jsonify(response.body), response.status_code
