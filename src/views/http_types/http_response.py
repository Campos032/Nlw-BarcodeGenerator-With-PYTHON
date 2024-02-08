# Importa o tipo Dict do módulo typing, usado para especificar o tipo dos argumentos e atributos da classe.
from typing import Dict

class HttpResponse:
    # Define o método construtor __init__, que inicializa objetos da classe. Ele aceita dois argumentos obrigatórios:
    # status_code, que é um número inteiro representando o código de status HTTP da resposta, e body, que é um
    # dicionário (Dict) representando o corpo da resposta.
    def __init__(self, status_code: int, body: Dict) -> None:
        # Atribui o argumento status_code ao atributo status_code do objeto HttpResponse.
        self.status_code = status_code
        # Atribui o argumento body ao atributo body do objeto HttpResponse.
        self.body = body

# Em resumo, esta classe fornece uma maneira de encapsular os dados de uma resposta HTTP em um único objeto
# HttpResponse, facilitando o envio de respostas consistentes e estruturadas em uma aplicação web.
        