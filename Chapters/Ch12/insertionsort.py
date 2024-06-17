def insertion_sort(values):
    for i in range(1, len(values)):
        next = values[i]

        # Sposta di una posizione in avanti tutti gli elementi precedenti > di next
        j = i
        while j > 0 and values[j - 1] > next :
            values[j] = values[j - 1]
            j = j -1
        # Inserisce l'elemento next nella posizione corretta
        values[j] = next

values = [10,9,8,7,6,3,1,2]
insertion_sort(values)
print(values)