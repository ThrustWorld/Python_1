from random import randint

def binary_search(list, element):
    start = 0 
    end = len(list) - 1
    while start < end: # Non abbiamo più controlli da fare se gli indici combaciano
        middle = (start + end) // 2 # Considerando che la lista deve essere già ordinata, possiamo partire a controllare da metà
        if list[middle] == element: # Se l'elemento corrisponde a quello della lista viene restituita la posizione
            return middle
        elif list[middle] < element:  # Se il nostro elemento è più grande, ci spostiamo di un indice a destra
            start = middle + 1
        elif list[middle] > element:
            end = middle - 1 # Se il nostro elemento è più piccolo, ci spostiamo di un indice a sinistra
    return -1

values = [1,5,21,46,50]
print(values)

element = randint(1,100)
print(element)

pos = binary_search(values,element)
if pos == -1:
    print("Element not in the list")
else:
    print("Element %d is in position %d" % (element,pos))