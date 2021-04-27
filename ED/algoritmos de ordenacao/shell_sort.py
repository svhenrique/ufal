import random
import time

def shell_sort(lista):
    h = 1
    while h<len(lista):
            if 3*h+1 < len(lista):
                    h = 3*h+1
            else:
                    break
    while h!=1:
            h = h//2
            for i in range(h,len(lista)):
                    aux = lista[i]
                    j = i
                    while lista[j-h]>aux:
                            lista[j] = lista[j-h]
                            j-=h
                            if j<h:
                                    break
                    lista[j] = aux
    return lista	

'''
for c in range(1, 6):
        lista = list(range(1, 100000))
        random.shuffle(lista)
        ini = time.time()
        a = shell_sort(lista)
        fim = time.time()
        print(fim-ini)
'''
'''
lista1 = list(range(1, 100001))
lista2 = list(range(100000, 0, -1))
lista3 = list(range(1, 100001))
random.shuffle(lista3)

lista4 = list(range(0, 10000))
lista5 = list(range(10000, 0))
lista6 = list(range(0, 10000))
random.shuffle(lista5)

listas = [lista1, lista2, lista3, lista4, lista5, lista6]

for c in listas:
    ini = time.time()
    shell_sort(c)
    fim = time.time()
    print(fim-ini)
'''
lista = [0.28, 0.3, 0.27, 0.33, 0.31]

lis = shell_sort(lista)
soma = sum(lis)
tam = len(lis)
media = soma/tam
vari = 0
for c in lis:
    vari += ((c - media)**2)
vari = vari/(media-1)
print(media)
print(vari)
    
