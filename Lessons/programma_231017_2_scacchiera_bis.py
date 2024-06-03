# Esercizio R3.9 (modificato)
#
# Si scriva un programma che prende in input la coordinata di una cella della
# scacchiera, nella notazione <lettera><numero> (ad esempio g3), e visualizzi
# il colore della cella.

# Questa versione si allontana dallo pseudo-codice dato in precedenza, e usa il
# trucco di incrementare il numero di riga nelle colonne a, c, e, g. In questo
# modo, il codice che funzione per le colonne b, d, f, h può essere usato anche
# per le altre colonne.

coordinate = input("Immetti coordinate casella: ")

colonna = coordinate[0]
riga = int(coordinate[1])

if colonna in "aceg":
    riga = riga + 1

if riga % 2 == 1:
    colore = "bianco"
else:
    colore = "nero"

print("Il colore dela casella è", colore)