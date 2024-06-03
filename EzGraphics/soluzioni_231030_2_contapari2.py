# Questa versione utilizza l'espressione condizionale := per semplificare
# il codice. L'espressione condizionale non fa parte del programma
# ufficiale del corso, potete quindi ignorare questa versione.
conta_pari = 0
while (n := int(input("Inserisci un numero: "))) >= 0:
    if n % 2 == 0:
        conta_pari += 1
print(f"Hai inserito {conta_pari} numeri pari")