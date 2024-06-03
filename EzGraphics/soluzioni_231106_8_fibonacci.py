n = int(input("Immettere valore n positivo: "))
if n == 0:
    # il numero di Fibonacci F(0) = 0
    print(0)
elif n == 1:
    # il numero di Fibonacci F(1) = 1
    print(1)
else:
    # Per calcolare la successione di Fibonacci, la formula da usare è
    # F(i) = F(i-1) + F(i-2)
    # Quindi, per calcolare il termine i-esimo di una successione, è necessario
    # sapere il termine i-1 esimo e il termino i-2 esimo. Questi due termini sono
    # memorizzati rispettivamente in fold1 ed fold2. Inizialmente i = 2, e quindi
    # F(i-1) = F(2-1) = F(1) = 1 per definizion ed F(i-2)= F(0) = 0 per definizione.
    # Per questo motivo le variabili fold1 ed fold2 sono inizializzate con 1 e 0.

    fold1 = 1
    fold2 = 0
    for i in range(2, n+1): # i varia da 2 ad n
        # Calcolo il nuovo termine F(i) della succession usando i due vecchi valori
        fnew = fold1 + fold2
        # Aggiorno le variabili fold. fold1 viene messo in fold2 ed il valore appena
        # calcolato in fold1 (fnew -> fold1 -> fold2). In questo modo, all'inizio del
        # prossimo ciclo, essi conterrano il valore precedente e il precedente del precedente.
        fold2 = fold1
        fold1 = fnew
    # Stampa l'ultimo numero di Fibonacci calcolato, ovvero F(n)
    print(fnew)