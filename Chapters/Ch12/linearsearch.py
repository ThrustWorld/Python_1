from random import randint

def linear_search(list, element):
    for i in range(len(list)): # Itera la lista alla ricerca dell'elemento
        if list[i] == element: # Se la ricerca trova l'elemento, ritorna la posizione occupata dall'elemento nella lista
            return i
    return -1

n = 10

values = []

for i in range(n):
    values.append(randint(1,100))

print(values)

done = False
while not done:
    element = int(input("Enter a number to search or -1 to quit: "))
    if element == -1:
        done = True
    else :
        pos = linear_search(values, element)
        if pos == -1:
            print("Element is not in the list")
        else:
            print("Element is in position %d" % pos)