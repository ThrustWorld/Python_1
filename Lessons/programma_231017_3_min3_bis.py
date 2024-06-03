# Programma che prende in input tre numeri positivi e calcola il minimo.
# Il programma si interrompe con un errore appena l'utente immette un
# valore negativo.

# Questa variante usa la funzione exit del modulo sys che stampa un messaggio
# e termina forzatamente l'esecuzione del programma. Grazie a questo, non è
# necessario usare tutti gli else della versione precedente e il programma
# è più lineare e leggibile.

import sys

n1 = int(input("Immetti primo numero: "))
if n1 < 0:
    sys.exit("Errore, n1 è negativo")

n2 = int(input("Immetti secondo numero: "))
if n2 < 0:
    sys.exit("Errore, n2 è negativo")

n3 = int(input("Immetti terzo numero: "))
if n3 < 0:
    sys.exit("Errore, n3 è negativo")

if n1 <= n2 and n1 <= n3:
    print(n1)
elif n2 <= n1 and n2 <= n3:
    print(n2)
else:
    print(n3)
