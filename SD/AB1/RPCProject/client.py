import grpc
import item_methods_pb2_grpc as pb2_grpc
import item_methods_pb2 as pb2


class ItemClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.ItemMethodsStub(self.channel)

    def pop_item(self, position):
        """
        Client function to call the rpc for PopItem
        """
        position = pb2.Position(position=position)
        print(f'Removendo item da posição {position}')
        return self.stub.PopItem(position)

    def get_itens(self):
        """
        Client function to call the rpc for GetItens
        """
        message = "get itens"
        message = pb2.Message(message=message)
        return self.stub.GetItens(message)

if __name__ == '__main__':
    client = ItemClient()
    itens = client.get_itens()
    print('-='*30)
    print(itens)
    position = int(input('Selecione qual item (por posicao) você quer deletar?: '))
    print('-='*30)
    result = client.pop_item(position=position)
    print(f'Item removido: {result}')
    print('-='*30)
    itens = client.get_itens()
    print('Itens restantes:')
    print(itens)
    print('-='*30)
