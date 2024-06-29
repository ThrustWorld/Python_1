def raddoppia(l, m):
    # Scorro con un ciclo for tutte le righe di m. Lo stesso indice viene usato anche
    # per scorrere gli elementi di l.
    for i in range(len(m)):
        # Per ogni riga i della matrice m, moltiplico per 2 l'elemento in colonna l[i]
        m[i][l[i]] *= 2
    # Non c'è nessun return perchè la funzione modifica direttamente la matrice m, non ne
    # crea una nuova.
