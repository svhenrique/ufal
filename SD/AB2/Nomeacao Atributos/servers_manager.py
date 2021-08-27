import json
import socket
from num_port import PORT

MANAGER_PORT = 65432

class ServerManager:

    servers = []
    HOST = '127.0.0.1'
    PORT = MANAGER_PORT # porta especifica para manager

    def _find_server_molde(self, instance, thing):
        found = []
        for server in self.servers:
            if instance == server[thing]:
                found.append(server)
        return found

    def _add_server(self, data_server):
        self.servers.append(data_server)

    def _receive_data(self, conn):
        data = conn.recv(1024)
        data = data.decode('utf_8')
        return data

    def _send_data_server(self, data, conn):
        servers = ''
        for server in data:
            server = json.dumps(server)
            servers += server + ';'
        servers = servers.encode('utf_8')
        conn.sendall(servers)

    def _find_by_name(self, instance):
        server = self._find_server_molde(instance, 'name')
        return server

    def _find_by_localization(self, instance):
        server = self._find_server_molde(instance, 'localization')
        return server

    def _find_by_attributes(self, instance):
        found = []
        for server in self.servers:
            if all(attribute in server['attributes'] for attribute in instance):
                found.append(server)
        return found

    def _find_server(self, instance, kind):
        if kind == 'name':
            data = self._find_by_name(instance)
        elif kind == 'attributes':
            data = self._find_by_attributes(instance)
        else:
            data = self._find_by_localization(instance)
        return data

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    data = self._receive_data(conn)
                    if data == 'client':
                        data = self._receive_data(conn)
                        data = json.loads(data)
                        kind, instance = data['kind'], data['instance']
                        servers = self._find_server(instance, kind)
                        self._send_data_server(servers, conn)
                        continue
                    elif data == 'shutdown':
                        server = self._receive_data(conn)
                        data = json.loads(data)
                        if server in self.servers:
                            self.servers.remove(server)
                        continue
                    data = json.loads(data)
                    port = PORT.return_new_port()
                    data['port'] = port
                    self._add_server(data)
                    conn.sendall(str(port).encode('utf_8'))
                    print(self.servers)



