
import socket
from validator import validar_cpf 

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# AF_INET - Internet address family for IPv4
# SOCK_STREAM -  Socket type for TCP

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            cpf = data.decode('utf_8')
            valid = validar_cpf(cpf)
            result = 'Valido' if valid is True else 'Invalido'
            conn.sendall(result.encode('utf_8'))
