# Programma che prende in input tre numeri positivi e calcola il minimo.
# Il programma si interrompe con un errore appena l'utente immette un
# valore negativo.

# In questa variante sono stati introdotti dei bug, che possono essere
# individuati tramite dei test (vedi notebook), e sono stati rimossi i
# controlli sui valori in input negativi.

n1 = int(input("Immetti primo numero: "))
n2 = int(input("Immetti secondo numero: "))
n3 = int(input("Immetti terzo numero: "))

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)
