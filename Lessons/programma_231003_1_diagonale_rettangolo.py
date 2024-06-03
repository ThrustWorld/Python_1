# Programma che prende in input la dimensione  dei due lati di un rettangolo e visualizza la lunghezza
# della diagonale.

# importo la funzione sqrt
from math import sqrt

base = float(input("Immetti base: "))
altezza = float(input("Immetti altezza: "))

# potre definire una variabile diagonale e metterci il risultato di sqrt(altezza ** 2 + base ** 2)
# ma, tanto per cambiare, preferisco mettere l'espressione che calcola il risultato direttamente
# dentro la funzione print.
print("La diagonale è", sqrt(altezza ** 2 + base ** 2))