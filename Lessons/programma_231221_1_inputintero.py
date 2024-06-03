def input_intero(prompt):
    """
    Visualizza la stringa passata nell'argomento prompt e prende in input da tastiera un numero
    intero. Se l'input NON è un intero, ripete la richiesta. Alla fine restituisce il numero
    immesso.
    """
    while True:
        # Ripeti per sempre
        try:
            # Prova a leggere il numero da tastiera e a convertirlo in intero
            n = int(input(prompt))
            # Se la stringa inserita dall'utente era effettivamente un intero, si arriva
            # a questo punto del programma e si esce dal ciclo while con la istruzione break
            break
        except ValueError:
            # Se la stringa inserita dall'utente non era un intero, viene catturata l'eccezione
            # di tipo ValueError che è stata generata e l'esecuzione arriva a questo punto, nel
            # quale stampiamo un messaggio di avvertimento
            print("Guarda che hai sbagliato!!")
            # Poiché l'eccezione è stata catturata, non genera l'interruzione del programma, e
            # quindi il while riparte da capo
    return n

n =input_intero("Immetti un numero, ma che sia un numero!: ")
print("Il numero immesso è", n)
