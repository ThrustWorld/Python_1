# In questa versione al posto di print("*" * i) uso un for per
# stampare una riga di i asterischi

n = int(input("Inserisci dimensione triangolo: "))
for i in range(1,n+1): # i varia da 1 fino ad n
    # questo ciclo for esegue per i volte l'istruzione di stampa di un asterisco
    for j in range(i):
         # end="" alla fine di questo print server per non andare a capo
        print("*", end="")
    # quando il for interno è terminato la riga di i asterischi è stata stampata e bisogna andare a capo
    print()
for i in range(n-1, 0, -1): # i varia da n-1 fino ad 1 (perché il valore finale è sempre escluso)
    for j in range(i):
        print("*", end="")
    print()
