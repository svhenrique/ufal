import logging

import threading

import time

import subprocess


"""
É importante destacar algumas coisas:
    1 - Essa é uma thread daemons, que vive apeanas enquanto o programa
    não é executado, após isso, ela é morta.
    2 - Como a thread é morta quando o programa é executado, a função
    thread_function não exige a ultima linha "finishing" pois ela é morta antes.
    3 - Se você rodar esse arquivo python com o IDLE ou derivados, a condição
    2 não e obedecida, pois o idle vai força-lo a printar o resto da função (e isso não
    é o correto). Porém, se for rodado no pront de comando (cmd), que é o modo correto
    de se abrir esse script, tudo funcionará normalmente.
"""

def thread_function(name):

    logging.info(f"Thread {name}: starting")
    subprocess.Popen('C:\Program Files\Microsoft\Edge\Application\msedge.exe')
    time.sleep(2)
    logging.info(f"Thread {name}: finishing")


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")


    logging.info("Main    : before creating thread")

    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    
    logging.info("Main    : before running thread")

    x.start()

    logging.info("Main    : wait for the thread to finish")

    # x.join()

    logging.info("Main    : all done")
