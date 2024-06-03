# Ripete l'input di un numero finché l'utente non ne inserisce uno positivo.
n = int(input("Inserisci un numero positivo: "))
while n < 0:
    print("Il numero deve essere positivo.")
    n = int(input("Inserisci un numero positivo: "))

# Questa parte è identica a quella dell'esercizio 1.
fact = 1
i = 2
while i <= n:
    fact *= i
    i += 1
print(f"Il fattoriale di {n} è {fact}")
