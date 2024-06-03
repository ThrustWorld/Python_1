n = int(input("Immetti numero intero positivo: "))
# facciamo variare candidato_primo da 2 fino ad n
for candidato_primo in range(2, n+1):
    # le istruzioni che seguono, fino alla riga 9, sono identiche a
    # quelle della soluzione dell'esercizio 6 (ma operano sulla variabile
    # candidato_primo invece che su n)
    primo = True
    for i in range(2, candidato_primo):
        if candidato_primo % i == 0:
            primo = False
            break
    # se primo è True vuole dire che candidato_primo è primo e lo stampo
    if primo:
        print(candidato_primo)
