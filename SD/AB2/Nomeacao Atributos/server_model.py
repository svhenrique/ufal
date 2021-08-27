from port import Port
import socket
from servers_manager import ServerManager, MANAGER_PORT
import json

class Server:

    host = '127.0.0.1'
    port = ''

    def __init__(self, name, attributes, localization):
        self.name = name
        self.attributes = attributes
        self.localization = localization
        self.socket = socket

    def _data_as_json(self):

        data = {
            'name': self.name,
            'attributes': self.attributes,
            'localization': self.localization,
        }
        data = json.dumps(data)
        return data.encode('utf-8')

    def _operantion(self, conn):
        data = conn.recv(1024)
        data = data.decode('utf_8')
        if '' != data:
            print(f'Data received: {data}')
            result = '1'
        else:
            result = '0'
        conn.sendall(result.encode('utf_8'))

    def _connect_with_master_server(self):
        with self.socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, MANAGER_PORT))
            data = self._data_as_json()
            s.sendall(data)
            port = s.recv(1024)
        port = port.decode('utf-8')
        self.port = int(port)

    def _shutdown_server(self, ):
        operation = 'shutdown'.encode('utf-8')
        with self.socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, MANAGER_PORT))
            s.sendall(operation)
            data = self._data_as_json()
            s.sendall(data)

    def start_server(self):
        self._connect_with_master_server()
        with self.socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    self._operantion(conn)

        # self._shutdown_server() linh de codigo inalcancavel
        # ao encerrar o servidor de forma bruta o servidor
        # nao consegue se desvinculr do manager
