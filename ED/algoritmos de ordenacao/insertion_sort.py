'''def insertion_sort(lista):
	for i in range(1,len(lista)):
		j = i
		while j>0 and lista[j]<lista[j-1]:
			lista[j],lista[j-1]=lista[j-1],lista[j]
			j-=1
	return lista
print(insertion_sort([1,2,3,4,5,6,7]))
'''
def selection(lista):
        for i in range(len(lista)):
                menor = i
                for j in range(i, len(lista)):
                        if lista[menor]>lista[j]:
                                menor = j
                lista[menor], lista[i] = lista[i], lista[menor]
        return lista
print(selection([2,8,4,6,1,9]))
