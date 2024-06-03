n = int(input("Immetti un numero: "))
while n > 0:
    # Utilizzo la variabile `prec` per salvare il valore della variabile
    # `n` della iterazione precedente.
    prec = n
    # Leggo il nuovo valore di n.
    n = int(input("Immetti un numero: "))
    # Controllo se i due valori coincidono.
    if n == prec:
        print("Hai inserito un numero duplicato")
