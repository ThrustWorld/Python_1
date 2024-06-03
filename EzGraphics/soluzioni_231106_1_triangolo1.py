# In questa versione uso print("*" * i) per stampre una riga
# formata da i asterischi.
n = int(input("Inserisci dimensione triangolo: "))
for i in range(1,n+1):  # i varia da 1 fino ad n
    # stampa una riga formata da i asterischi
    print("*" * i)
for i in range(n-1, 0, -1): # i varia da n-1 fino ad 1 (perché il valore finale è sempre escluso)
    # stampa una riga formata da i asterischi
    print("*" * i)