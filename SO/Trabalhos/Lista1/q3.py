class Cliente:
    nome = ''
    saldo = 0

    def __init__(self, nome, saldo):
        self.nomoe = nome
        self.saldo = saldo

def processo1(clienteA, clienteB):
    
    # saque em A
    x = clienteA.saldo
    x = x - 200
    clienteA.saldo = x

    # saque em B
    x = clienteB.saldo
    x = x + 100
    clienteB.saldo = x
    
def processo2(clienteA, clienteB):

    # saque em A
    y = clienteA.saldo
    y = y - 100
    clienteA.saldo = y

    # deposito em B
    y = clienteB.saldo
    y = y + 200
    clienteB.saldo = y
"""
Resposta letra a

clienteA = Cliente('A', 500)
clienteB = Cliente('B', 900)

processo1(clienteA, clienteB)
processo2(clienteA, clienteB)
print(clienteA.saldo)
print(clienteB.saldo)

"""

"""
Resposta letra b
1a, 2a, 1b, 2b, 1c, 2c, 1d, 2d, 1e, 2e, 1f, 2f

clienteA = Cliente('A', 500)
clienteB = Cliente('B', 900)

1a: x = clienteA.saldo (500) 
2a: y = clienteA.saldo (500)

1b: x = x - 200 = 500 - 200 = 300 
2b: y = y - 100 = 500 - 100 = 400

1c: clienteA.saldo = x (300)
2c: clienteA.saldo = y (400)
clienteA.saldo ficou como 400 pois o ultimo prevalece

1d: x = clienteB.saldo (900)
2d: y = clienteB.saldo (900)

1e: x = x + 100 = 900 + 100 = 1000
2e: y = y + 100 = 900 + 200 = 1100

1f: clienteB.saldo = 1000
2f: clienteB.sald = 1100
clienteB.saldo ficou como 1100 pois o ultimo prevalece

Resposta:
    saldo de cliente A: 400
    saldo de cliente B: 1100
"""

