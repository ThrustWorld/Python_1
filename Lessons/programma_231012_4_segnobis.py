# Programma che prende in input un numero intero e stampa se è positivo,
# negativo o nullo.

# Versione senza if annidati

numero = int(input("Immetti un numero: "))
if numero > 0:
    print("positivo")
if numero == 0:
    print("zero")
if numero < 0:
    print("negativo")

# È importante in questo caso che le scelte siano tra di loro esclusive.