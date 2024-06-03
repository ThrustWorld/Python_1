# Programma che prende in input un numero intero e stampa il suo valore assoluto.
# Realizzato senza far uso della funzione `abs` in modo da dover sfruttare
# l'istruzione if.

numero = int(input("Immetti numero: "))
if numero > 0:
    risultato = numero
else:
    risultato = -numero
print("Il valore assoluto è", risultato)
