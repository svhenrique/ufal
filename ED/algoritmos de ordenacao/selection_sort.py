def selection_sort(lista):
	#para cada item
	for i in range(len(lista)): 
		#procure o menor elemento a partir do item
		menor = i
		for j in range(i,len(lista)):
			if lista[j]<lista[menor]:
				menor = j
		#troque de posicao com o item
		lista[i],lista[menor] = lista[menor],lista[i]
	return lista

print(selection_sort([3,9,5,8,4,0,2,-1,-2]))
