# Eserczio R3.18 (modificato)
# Scrivere un programma che prende in input un voto tra 1 e 100, e stampa un voto
# in lettere secondo la seguente tabella di corrispondenza
#
#  90-100  A
#  80-89   B
#  70-79   C
#  60-69   D
#  <  60   F

# Questa variante non usa né else né elif. Bisogna però controllare per
# ogni intervallo sia l'estremo superiore che inferiore.

voto = int(input("Immetti voto da 1 a 100: "))

if voto >= 90:
    print("A")
if voto >= 80 and voto <= 89:
    print("B")
if voto >= 70 and voto <= 79:
    print("C")
if voto >= 60 and voto <= 69:
    print("D")
if voto < 60:
    print("F")

print("Ciao sono uscito dall'if")
