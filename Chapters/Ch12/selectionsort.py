from random import randint
from time import time

def selection_sort(values):
    for i in range(len(values)):
        min_pos = minimum_position(values, i)
        # Scambia le posizioni dei due elementi
        temp = values[min_pos]
        values[min_pos] = values[i]
        values[i] = temp

def minimum_position(values, start):
    min_pos = start
    for i in range(start + 1, len(values)): # Controlla tutta la lista ritornando l'elemento più piccolo
        if values[i] < values[min_pos]:
            min_pos = i

    return min_pos

n = 10
values = []
for i in range(n):
    values.append(randint(1, 100))

print(values)
start_time = time()
selection_sort(values)
print(values)
end_time = time()
print("Time: %.3f" %(end_time-start_time))