# costante con lo spazio da assegnare ad ogni numero nella tabella
SIZE = 6
n = int(input("Immetti dimensione tavola: "))

## stampa intestazione della tabella
# stampa prima colonna della riga di intestazione (solo spazi)
print(f"{' ':{SIZE}}", end="")
# stampa le restanti colonne della riga di intestazione
for i in range(1,n+1):
    print(f"{i:{SIZE}}", end="")
# va a capo alla fine di ogni riga
print()

## stampa tabella vera e propria
for j in range(1, n+1):
    # stampa la prima colonna della tabella
    print(f"{j:{SIZE}}", end="")
    # stampa il resto delle colonne della tabella
    for i in range(1, n+1):
        print(f"{i * j:{SIZE}}", end="")
    # va a capo alla fine di ogni riga
    print()
