def insertion_sort(lista):
	for i in range(1,len(lista)):
		j = i
		while j>0 and lista[j]<lista[j-1]:
			lista[j],lista[j-1]=lista[j-1],lista[j]
			j-=1
	return lista
print(insertion_sort([1,2,3,4,5,6,7]))


