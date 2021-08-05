import logging
import grpc
from concurrent import futures
import item_methods_pb2_grpc as pb2_grpc
import item_methods_pb2 as pb2
import bd

class ItemService(pb2_grpc.ItemMethodsServicer):

    def __init__(self, *args, **kwsargs):
        pass

    def PopItem(self, request, context):

        # get the position from the incoming request
        position = request.position
        poped_item = bd.produtos.pop(position)

        # verificar se não tem que ser um dict como no site
        # https: // www.velotio.com / engineering - blog / grpc - implementation - using - python
        result = {'name': poped_item}
        return pb2.Item(**result)

    def GetItens(self, request, context):

        # get produtos in list
        itens_in_bd = bd.produtos

        # transforming list itens_in_bd for string
        itens = " | ".join(itens_in_bd)
        result = {'message': itens}
        return pb2.Message(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ItemMethodsServicer_to_server(
        ItemService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()