import json

class Comunication:

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

class Helo(Comunication):
    pass

class Mail(Comunication):
    pass

class Rcpt(Comunication):
    pass

class Data(Comunication):
    pass