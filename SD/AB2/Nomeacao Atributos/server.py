from server_model import Server

if __name__ == "__main__":
    name = input('Digite um nome para o servidor: ').lower()
    attributes = input('Digite os atributos (virgula entre atributos): ').lower().split(',')
    localization = input('Digite a localizacao do servidor: ').lower()
    server = Server(name, attributes, localization)
    server.start_server()
    print('SERVIDOR {server.name} ENCERRADO')