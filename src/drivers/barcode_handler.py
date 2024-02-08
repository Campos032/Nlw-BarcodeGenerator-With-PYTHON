# Importa a classe Code128 do módulo barcode. Essa classe é responsável por gerar códigos de barras do tipo Code128.
from barcode import Code128
# Importa a classe ImageWriter do módulo barcode.writer. Essa classe é usada para escrever o código de barras gerado
# em um arquivo de imagem.
from barcode.writer import ImageWriter

# Define uma classe chamada BarcodeHandler que encapsula a funcionalidade de lidar com códigos de barras.
class BarcodeHandler:
    # Define um método chamado create_barcode que recebe um parâmetro product_code do tipo str e retorna um caminho
    # (str) para o arquivo de imagem do código de barras gerado.
    def create_barcode(self, product_code: str) -> str:
        # Cria uma instância da classe Code128, passando o product_code como argumento e especificando o ImageWriter()
        # para escrever a imagem do código de barras.
        tag = Code128(product_code, writer=ImageWriter())
        # Converte o objeto tag em uma string e armazena em path_from_tag. Isso geralmente retorna a representação do
        # objeto, que inclui o tipo do código de barras e o código do produto.
        path_from_tag = f'{tag}'
        # Salva o código de barras como uma imagem no caminho especificado em path_from_tag.
        tag.save(path_from_tag)
        # Retorna o caminho onde o arquivo de imagem do código de barras foi salvo.
        return path_from_tag
        