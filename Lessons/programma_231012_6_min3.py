# Programma che prende in input tre numeri e stampa il minimo dei tre.

n1 = int(input("Immetti primo numero"))
n2 = int(input("Immetti secondo numero"))
n3 = int(input("Immetti terzo numero"))

if n1 < n2:
    # Se siamo qui, il minimo è sicuramente uno tra n1 ed n3.
    if n1 < n3:
        min_valore = n1
    else:
        min_valore = n3
else:
    # Se siamo qui vuol dire che n2 <= n1, quindi il minimo è sicuramente
    # uno tra n2 ed n3.
    if n2 < n3:
        min_valore = n2
    else:
        min_valore = n3

print("Il minimo è", min_valore)