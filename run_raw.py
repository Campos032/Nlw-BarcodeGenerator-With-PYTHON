# Importa as classes Flask, jsonify e request do framework Flask. Flask é o framework web utilizado para criar o
# aplicativo, jsonify é usado para serializar objetos Python em formato JSON e request é usado para acessar os dados
# enviados com a requisição HTTP.
from flask import Flask, jsonify, request
# Importa a classe Code128 do módulo barcode, que é usado para gerar códigos de barras no formato Code 128.
from barcode import Code128
# Importa a classe ImageWriter do módulo barcode.writer, usado para salvar o código de barras como uma imagem.
from barcode.writer import ImageWriter

# Cria uma instância do aplicativo Flask.
app = Flask(__name__)

# Define uma rota /create_tag para o método POST. Isso significa que esta rota irá manipular requisições POST enviadas
# para /create_tag.
@app.route('/create_tag', methods=['POST'])
# Define a função create_tag, que será executada quando uma requisição POST for enviada para /create_tag.
def create_tag():
    # Obtém os dados enviados com a requisição POST no formato JSON.
    body = request.json
    # Obtém o código do produto do corpo da requisição.
    product_code = body.get('product_code')

    # Cria um objeto Code128 com o código do produto fornecido.
    tag = Code128(product_code, writer=ImageWriter())
    # Define o caminho da tag como a representação de string do objeto Code128.
    path_from_tag = f'{tag}'
    # Salva a tag de código de barras como uma imagem no caminho especificado.
    tag.save(path_from_tag)
    # Retorna a resposta da requisição como um objeto JSON, contendo o caminho da tag de código de barras gerada.
    return jsonify({"tag_path": path_from_tag})

# Verifica se o script está sendo executado diretamente pelo interpretador Python.
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento embutido do Flask, tornando o aplicativo Flask disponível na porta 3000 para
    # todas as interfaces de rede.
    app.run(host='0.0.0.0', port=3000)

# Em resumo, este código cria um aplicativo Flask que fornece uma rota POST /create_tag para gerar tags de código de
# barras com base em um código de produto fornecido no corpo da requisição. A tag gerada é salva como uma imagem e o
# caminho da tag é retornado como uma resposta JSON.
