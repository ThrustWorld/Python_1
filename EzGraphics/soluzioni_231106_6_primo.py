n = int(input("Immetti numero intero positivo: "))
# attenzione, il numero 1 non è primo e va trattato a parte
if n <= 1:
    primo = False
else:
    # Il tutto funziona come il programma per determinare se una stringa
    # è palindroma. La variabile primo ci dice se, per quanto ne sappiamo,
    # il numero n può essere primo. Inizialmente è True, ma non appena troviamo
    # un divisore, sappiamo che non può essere primo e la mettiamo a False.
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            # facciamo anche un break, per uscire dal ciclo, tanto a
            # questo punto sappiamo che n non è primo, inutile controllare altri
            # divisori
            break
print(n, "è primo" if primo else "non è primo")