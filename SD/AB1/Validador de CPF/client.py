
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    cpf = input('Digite o CPF para verificar validação (só os números): ')
    s.sendall(cpf.encode('utf_8'))
    data = s.recv(1024)

print(data.decode('utf_8'))
