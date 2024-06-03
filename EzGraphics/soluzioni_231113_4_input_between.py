def input_between(prompt, a, b):
    """
    Legge da tastiera un numero intero e lo restituisce al chiamante, accertandosi che il valore
    sia compreso tra 'a' e 'b' (estremi inclusi). Finché l'utente non inserisce un valore corretto, gli
    verrà richiesto di inserire un nuovo numero. La variabile 'prompt' contiene il messaggio da
    visualizzare all'utente come prompt per il valore in input.
    """
    # Visualizzo il messaggio presente nella variabile prompt e prendo in input un intero.
    x = int(input(prompt))
    # Il ciclo while continua fino a quando l'utente immette un numero nell'intervallo [a,b].
    while x < a or x > b:
        print("Errore nell'inserimento")
        x = int(input(prompt))
    # Quando finalmente l'utente ha immesso un valore che va bene, si esce dal ciclo while
    # e restituisc il valore immesso dall'utente.
    return x

x = input_between("Immetti un numero: ", 1, 10)
print("Hai inserito il numero", x)