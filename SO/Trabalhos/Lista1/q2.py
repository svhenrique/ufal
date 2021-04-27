import logging
import threading
import time
import concurrent.futures

import random

fontes = """
    https://stackoverflow.com/questions/11421651/controlling-scheduling-priority-of-python-threads
"""

class Bola:

    crianca = ''
    

class Crianca:

    numero = ''
    bola = None
    dominio = 3 
    habilidae = 0 # variavel para simular prioridade de thread
    
    def __init__(self, numero):
        self.numero = numero
        self.habilidade = random.randint(0, 5)
                
    def _pegar_a_bola(self, bola):
        logging.info(f"Jogador {self.numero}: Pegou a bola")
        self.bola = bola
        self.bola.crianca = self.numero

    def _passar_a_bola(self, crianca):
        crianca._pegar_a_bola(self.bola)
        self.bola = None
        
    def _tempo_de_dominio(self):
        return self.dominio + self.habilidade
    
    def dominio_de_bola(self, crianca):
        logging.info(f"Jogador {self.numero}: Tá dominando a bola")
        time.sleep(self._tempo_de_dominio())
        if crianca.numero != 11:    
            logging.info(f"Jogador {self.numero}: Passou a bola")
            self._passar_a_bola(crianca)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    criancas = []
    bola = Bola()

    logging.info("Comeeeeeeeeçaaaaaaaaa o jogo")

    # primeiro movimento do jogo
    atual = Crianca(1)
    atual._pegar_a_bola(bola)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as jogadores:
        for jogador in range(1, 11):
            proximo = Crianca(jogador+1)
            jogadores.submit(atual.dominio_de_bola(proximo), jogador)
            atual = proximo

    logging.info(f"Jogador {jogador} chuta")
    logging.info("E é GOOOOOOOOLLLLLL!!!!!!")
    


