import time
import random

def merge_sort(lista):
	return divisao(lista)

def divisao(lista):
	#dividir a lista
	lista1 = lista2=[]
	if len(lista)>1:
		meio = len(lista)//2
		lista1 = divisao(lista[0:meio])
		lista2 = divisao(lista[meio:])
		return combinacao(lista1,lista2)
	else:
		return lista

def combinacao(lista1,lista2):
	i = j = 0
	lista = []
	for c in range(len(lista1)+len(lista2)):
		if i == len(lista1):
			lista.append(lista2[j])
			j+=1

		elif j == len(lista2):
			lista.append(lista1[i])
			i+=1

		elif lista1[i]<lista2[j]:
			lista.append(lista1[i])
			i+=1
		else:
			lista.append(lista2[j])
			j+=1
	return lista
'''
for c in range(1, 6):
        lista = list(range(1, 100000))
        random.shuffle(lista)
        ini = time.time()
        a = merge_sort(lista)
        fim = time.time()
        print(fim-ini)
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
    merge_sort(c)
    fim = time.time()
    print(fim-ini)
	
