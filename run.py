# Importa a instância do aplicativo Flask do módulo server localizado no diretório src/main/server. Esta instância do
# aplicativo Flask representa a aplicação web que você construiu.
from src.main.server.server import app

# Verifica se o script está sendo executado diretamente como o ponto de entrada principal do programa.
if __name__ == '__main__':
    # Inicia o servidor Flask. Ele define o host para '0.0.0.0', o que significa que o servidor estará disponível em
    # todas as interfaces de rede. O número da porta é definido como 3000. O modo de depuração está habilitado para
    # permitir o rastreamento de erros e recarregar automaticamente o servidor quando o código é modificado. Isso é
    # útil durante o desenvolvimento, mas deve ser desativado em um ambiente de produção.
    app.run(host='0.0.0.0', port=3000, debug=True)

# Em resumo, este código inicia o servidor Flask, permitindo que sua aplicação web seja acessada em um navegador ou
# por requisições HTTP de outros clientes.
    