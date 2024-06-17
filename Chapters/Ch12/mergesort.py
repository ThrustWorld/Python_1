from random import randint

def merge_sort(list):
    if len(list) <= 1 : return # Casp speciale: lista con un solo elemento
    half = len(list) // 2 # Divisione della lista in due
    first_half = list[ : half] # prima metà della lista
    second_half = list[half : ] # seconda metà della lista
    merge_sort(first_half) # Stesso procedimento di suddivisione sulla prima metà
    merge_sort(second_half) # Stesso procedimento di suddivisione sulla seconda metà
    merge_lists(first_half, second_half, list) # Fusione delle sottoliste in liste ordinate

def merge_lists(first_half, second_half, list):
    i = 0 # indice prima lista
    j = 0 # indice seconda lista
    k = 0 # indice della fusione
    while i < len(first_half) and j < len(second_half): # Controlliamo gli elementi finchè uno degli indici non ha controllato tutta la lista
        if first_half[i] < second_half[j]: # Ricerca elemento più piccolo tra le liste e aggiunta di esso nella fusione
            list[k] = first_half[i]
            i += 1 # Spostamento indice
            k += 1 # Spostamento indice
        elif second_half[j] < first_half[i]:
            list[k] = second_half[j]
            j += 1
            k += 1
    
    # Controlliamo quale delle due liste ha ancora elementi e li aggiungiamo alla fusione
    while i < len(first_half):
        list[k] = first_half[i]
        i +=  1
        k += 1
    
    while j < len(second_half):
        list[k] = second_half[j]
        j += 1
        k += 1

n = 5
values = []
for i in range(n):
    values.append(randint(1, 100))

print(values)
merge_sort(values)
print(values)