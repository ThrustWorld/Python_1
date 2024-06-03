# Questa versione è derivata direttamente dal programma che calcola la somma
# dei numeri da 1 a 1000 visto a lezione.
n = int(input("Inserisci un numero: "))
fact = 1
i = 2 # inizializzato a 2, ma andrebbe bene anche inizializzato a 1
while i <= n:
    fact *= i
    i += 1
print(f"Il fattoriale di {n} è {fact}")
