#  Importa o tipo Dict do módulo typing, usado para especificar o tipo dos argumentos e atributos da classe.
from typing import Dict

# Define o método construtor __init__, que inicializa objetos da classe. Ele aceita três argumentos opcionais: header,
# body e query_params, todos eles sendo dicionários (Dict) que representam os cabeçalhos, corpo e parâmetros de
# consulta da requisição, respectivamente.
class HttpRequest:
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None
        ) -> None:
        # Atribui o argumento header ao atributo header do objeto HttpRequest.
        self.header = header
        # Atribui o argumento body ao atributo body do objeto HttpRequest.
        self.body = body
        # Atribui o argumento query_params ao atributo query_params do objeto HttpRequest
        self.query_params = query_params

# Em resumo, essa classe fornece uma maneira de encapsular os dados de uma requisição HTTP em um único objeto
# HttpRequest, facilitando o manuseio e a passagem desses dados em uma aplicação web.
    