saldo = float(input("Immetti saldo iniziale: "))
tasso = float(input("Immetti tasso di interesse: "))
# L'istruzione += che è un modo abbreviato di aggiungere un valore ad una
# variabile. "var += exp" equivale a "var = var + exp".
# Utilizziamo sempre la stessa variabile saldo che incrementiamo con
# gli interessi anno dopo anno.
saldo += saldo * tasso / 100
# Notare che ci sono due spazi dopo "anno:", mentre nelle print successive
# c'è solo una spazio dopo "anni:". Questo perché dobbiamo assicurarci che
# "{saldo:10.2f}" inizia sempre alla stessa colonna perché il risultato sia
# allineato.
print(f"Dopo un anno:  {saldo:10.2f}")
saldo += saldo * tasso / 100
print(f"Dopo due anni: {saldo:10.2f}")
saldo += saldo * tasso / 100
print(f"Dopo tre anni: {saldo:10.2f}")
