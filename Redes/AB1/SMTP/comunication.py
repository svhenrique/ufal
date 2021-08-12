import json

class Helo:

    @staticmethod
    def send(socket, **data):
        data = json.dumps(data)
        data = data.encode(encoding='utf-8')
        try:
            socket.sendall(data)
        except Exception as e:
            print(e)

    @staticmethod
    def receive(socket):
        try:
            data = socket.recv(1024)
            data = data.decode(encoding='utf-8')
            data = json.loads(data)
            return data
        except Exception as e:
            print(e)

