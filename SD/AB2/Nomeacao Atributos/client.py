import json
import socket
from servers_manager import ServerManager, MANAGER_PORT

SERVER_MANAGER = ServerManager()
HOST = '127.0.0.1'  # The server's hostname or IP address

print('[0] - Procurar servidor por nome')
print('[1] - Procurar servidor por atributo')
print('[2] - Procurar servidor por localizacao')

choice = input('O que deseja fazer?: ')
while choice not in ['0', '1', '2']:
    choice = input('O que deseja fazer?: ')
choice = int(choice)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, MANAGER_PORT))
    data = 'client'
    s.sendall(data.encode('utf_8'))

    if choice == 0:
        instance = input('Digite o nome do servidor que deseja: ')
        kind = 'name'
    elif choice == 1:
        instance = input('Digite o atributo(s) do servidor que deseja (separe por virgula atributos diferentes): ').strip().split(',')
        kind = 'attributes'
    elif choice == 2:
        instance = input('Digite a localizacao do servidor que deseja: ')
        kind = 'localization'

    data = json.dumps({'instance': instance, 'kind': kind})
    s.sendall(data.encode('utf_8'))

    servers = s.recv(1024).decode('utf-8')

servers = servers.split(';')
del servers[-1]

if len(servers) == 0:
    print('Nenhum servidor encontrado')
    exit()

print('=-'*5, 'SERVIDORES DISPONIVEIS', '=-'*5)
for index_server in range(len(servers)):
    print(f'[{index_server}] - {servers[index_server]}')
print('=-'*25)

choice = int(input('Escolha o servidor pelo numero representado a esquerda: '))

if choice < 0 or choice > len(servers):
    print('Servidor invalido.')
    exit()

chosen_server = json.loads(servers[choice])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, chosen_server['port']))
    data = input('Digite alguma coisa: ')
    s.sendall(data.encode('utf_8'))
    data = s.recv(1024)

print(data.decode('utf_8'))
