def bubble_sort(lista: list) -> None:
    n = len(lista)
    for i in range(n):
    
        for j in range(0, n-i-1):
            
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


lista = [7, 9, 6, 5, 8, 4, 3, 2, 1, 10]
bubble_sort(lista)
print("Lista ordenada:", lista)
