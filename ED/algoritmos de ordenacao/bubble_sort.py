def bubble_sort(lista):
	comp = 0
	for i in range(len(lista)-1):
		for j in range(len(lista)-1-i):
			comp+=1
			if lista[j]>lista[j+1]:
				lista[j],lista[j+1]=lista[j+1],lista[j]
	print(comp)
	return lista

print(bubble_sort([7,6,5,4,3,2,1]))































# def bubble_sort(lista):
# 	for i in range(len(lista)-1):
# 		for j in range(len(lista)-1-i):
# 			if lista[j]>lista[j+1]:
# 				lista[j],lista[j+1] = lista[j+1],lista[j]
# 	return lista

# print(bubble_sort([3,9,5,8,4,0,2]))