# Eserczio R3.18 (modificato)
# Scrivere un programma che prende in input un voto tra 1 e 100, e stampa un voto
# in lettere secondo la seguente tabella di corrispondenza
#
#  90-100  A
#  80-89   B
#  70-79   C
#  60-69   D
#  <  60   F

# Questa variante usa la clausola elif per evitare livelli di indentazione
# eccessivi.

voto = int(input("Immetti voto da 1 a 100: "))

if voto >= 90:
    print("A")
elif voto >= 80:
    print("B")
elif voto >= 70:
    print("C")
elif voto >= 60:
    print("D")
else:
    print("F")

print("Ciao sono uscito dall'if")