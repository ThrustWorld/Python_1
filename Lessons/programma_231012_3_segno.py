# Programma che prende in input un numero intero e stampa se è positivo,
# negativo o nullo.

numero = int(input("Immetti un numero: "))
if numero > 0:
    print("positivo")
else:
    # se siamo qui, vuol dire che numero è 0 oppure negativo
    # usiamo un altro if annidato
    if numero == 0:
        print("zero")
    else:
        print("negativo")
    # questa istruzione non serve a nulla, ma serve a mostrare che
    # se il numero immesso è <= 0, dopo l'istruzione `if numero == 0`
    # si arriva a questo punto del programma
    print("sono qua")

# questa istruzione non serve a nulla, tranne mostrare che, indipendentemente
# dal valore di numero, si arriva alla fine a questo punto del programma.
print("programma finito")
