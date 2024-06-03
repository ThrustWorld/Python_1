conta_pari = 0
# lettura di preparazione prima di entrare nel ciclo
n = int(input("Inserisci un numero: "))
while n >= 0:
    if n % 2 == 0:
        conta_pari += 1
    # lettura di aggiornamento
    n = int(input("Inserisci un numero: "))
print(f"Hai inserito {conta_pari} numeri pari")