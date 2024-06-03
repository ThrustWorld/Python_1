# Programma che prende in input due numeri interi, e stampa sia il minimo
# che il massimo dei due.

n1 = int(input("Immetti primo numero: "))
n2 = int(input("Immetti secondo numeri: "))

if n1 > n2:
    valore_max = n1
    valore_min = n2
else:
    valore_max = n2
    valore_min = n1

print("Il valore massimo è", valore_max)
print("Il valore minimo è", valore_min)
