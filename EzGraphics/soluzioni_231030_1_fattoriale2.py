# Questa versione utilizza direttamente la variabile n come contatore,
# cha parte dal valore iniziale immesso dall'utente e viene decrementato
# fino a 2.
n = int(input("Inserisci un numero: "))
fact = 1
while n >= 2:
    fact *= n
    n -= 1
# non posso stampare il valore iniziale di n perché l'ho perso
print("Il fattoriale è", fact)