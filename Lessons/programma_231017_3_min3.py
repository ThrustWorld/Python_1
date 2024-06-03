# Programma che prende in input tre numeri positivi e calcola il minimo.
# Il programma si interrompe con un errore appena l'utente immette un
# valore negativo.

n1 = int(input("Immetti primo numero: "))
if n1 < 0:
    print("Errore, n1 è negativo")
else:
    n2 = int(input("Immetti secondo numero: "))
    if n2 < 0:
        print("Errore, n2 è negativo")
    else:
        n3 = int(input("Immetti terzo numero: "))
        if n3 < 0:
            print("Errore, n3 è negativo")

        if n1 <= n2 and n1 <= n3:
            print(n1)
        elif n2 <= n1 and n2 <= n3:
            print(n2)
        else:
            print(n3)
