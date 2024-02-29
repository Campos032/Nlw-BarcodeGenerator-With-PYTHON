#  Importa a classe HttpResponse do módulo http_response localizado no pacote src/views/http_types. Esta classe
#  representa uma resposta HTTP.
from src.views.http_types.http_response import HttpResponse
# Importa a classe HttpUnprocessableEntityError do módulo http_unprocessable_entity localizado no pacote
# src/errors/error_types. Esta classe representa um erro específico de entidade não processável em uma solicitação HTTP.
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

# Define uma função chamada handle_errors que recebe um parâmetro error do tipo Exception e retorna um objeto
# HttpResponse. Esta função é responsável por lidar com erros e retornar uma resposta HTTP apropriada.
def handle_errors(error: Exception) -> HttpResponse:
    # Verifica se o erro recebido é uma instância da classe HttpUnprocessableEntityError.
    if isinstance(error, HttpUnprocessableEntityError):
        # Enviar para um log
        # enviar para um email de notificação
        # Retorna uma resposta HTTP com um código de status e corpo apropriados, dependendo do tipo de erro:
        # Se o erro for do tipo HttpUnprocessableEntityError, ele cria uma resposta com o código de status especificado
        # pelo erro e detalhes fornecidos pelo erro.
        # Caso contrário, cria uma resposta genérica de erro do servidor com o código de status 500 e uma mensagem de
        # erro genérica.
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
        
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )

# Essa função handle_errors é um exemplo de como você pode tratar diferentes tipos de erros de uma maneira
# personalizada e retornar respostas HTTP adequadas para e
