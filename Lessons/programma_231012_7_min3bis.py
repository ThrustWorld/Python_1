# Programma che prende in input tre numeri e stampa il minimo dei tre.

n1 = int(input("Immetti primo numero"))
n2 = int(input("Immetti secondo numero"))
n3 = int(input("Immetti terzo numero"))

min_valore = n3
if n1 < n2:
    if n1 < n3:
        min_valore = n1
else:
    if n2 < n3:
        min_valore = n2

print("Il minimo è", min_valore)