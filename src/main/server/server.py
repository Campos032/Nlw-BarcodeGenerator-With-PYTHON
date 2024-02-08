# Importa a classe Flask do framework Flask, usada para criar uma instância da aplicação web Flask.
from flask import Flask
# Importa o objeto tag_routes_bp, que é um Blueprint contendo as rotas relacionadas a tags, do módulo tag_routes
# localizado no diretório src/main/routes.
from src.main.routes.tag_routes import tag_routes_bp

# Cria uma instância da classe Flask, representando a aplicação web Flask. O parâmetro __name__ é usado para determinar
# o nome do pacote principal, necessário para localizar recursos estáticos e templates.
app = Flask(__name__)

# Registra o Blueprint tag_routes_bp na aplicação Flask. Isso faz com que todas as rotas definidas dentro do Blueprint
# estejam disponíveis para a aplicação Flask.
app.register_blueprint(tag_routes_bp)

# Em resumo, este código configura uma aplicação Flask e registra as rotas relacionadas a tags definidas no Blueprint
# tag_routes_bp, permitindo que a aplicação responda a requisições HTTP para essas rotas.
