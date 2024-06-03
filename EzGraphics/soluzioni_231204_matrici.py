# In questo file trovate tutte le soluzioni agli esercizi del 4 dicembre 2023

# Esercizio 0
# La soluzione di questo esercizio è in realtà già presente nel notebook del
# 30 novembew 2023 col nome di somma_righe2
def somma_righe2(l):
    risultato = [ ]
    for riga in l:
        somma = 0
        for elemento in riga:
            somma += elemento
        risultato.append(somma)
    return risultato

# Esercizio 1
# Questa prima versione è basata su somma_righe (vedi notebook del 30 novembre 2023),
# invertendo però i due for: quello esterno conta adesso le colonne, quello interno
# conta le righe. In questo modo gli elementi della matrice vengono visitati per colonne
# (prima la colonna 0, poi quella 1, e così via)
def somma_colonne(l):
    risultato = []
    # Poiché per ipotesti le righe hanno tutte lo stesso numero di colonne, possiamo
    # semplicemente determinare il numero di colonne calcolando la lunghezza della
    # prima riga.
    for num_colonna in range(len(l[0])):
        somma = 0
        # Come sempre, il numero di elementi di l corrisponde al numero di righe
        for num_riga in range(len(l)):
            somma += l[num_riga][num_colonna]
        risultato.append(somma)
    return risultato

# Esercizio 1 bis
# Questa versione è invece basata su somma_righe3. Poiché iniciamo creando la lista
# risultato già col numero corretto di elementi, non è necessario invertire i due
# for. Possiamo continuare ad esplorare le colonne nell'ordine consueto (una riga alla
# volta), pur di sommare gli elementi alla posizione corretta del risultato.
def somma_colonne_bis(l):
    # La lunghezza della lista risultato è uguale al numero di colonne di l, ovvero
    # il numero di elementi della prima riga di l.
    risultato = [0] * len(l)
    for num_riga in range(len(l)):
        for num_colonna in range(len(l[num_riga])):
            # importaten somma l'elemento in posizione (num_riga, num_colonna) alla
            # posizione corretta di risultato, che dipende dal numero di colonna.
            risultato[num_colonna] += l[num_riga][num_colonna]
    return risultato

# Esercizio 2
def fill_table(l,v):
    # Scorre tutti gli elementi della matrice `l` e li rimpiazza con v
    for num_riga in range(len(l)):
        for num_colonna in range(len(l[num_riga])):
            l[num_riga][num_colonna] = v

# Esercizio 3
def somma_matrici(a, b):
    # Scorre tutti gli elementi della matrice `a`, e ad essi somma l'elemento
    # della matrice `b` che si trova nella stessa posizione.
    for num_riga in range(len(a)):
        for num_colonna in range(len(a[num_riga])):
            a[num_riga][num_colonna] += b[num_riga][num_colonna]

# Questa funzione, anche se direttamente non risolve nessun esercizio,  viene
# utilizzata dalle funzioni matrice_identica e tavola_pitagorica per creare una
# matrice riempita con zeri.
def crea_matrice(num_righe, num_colonne):
    """
    Crea una matrice di `num_righe` righe e `num_colonne` colonne tutta riempita con 0.
    """
    risultato = [ ]
    for _ in range(num_righe):
        risultato.append([0] * num_colonne)
    return risultato

# Esercizio 4
# Questa versione si basa sulla funzione ausiliaria crea_matrice.
def matrice_identica(n):
    # Creo una matrice piena di 0
    m = crea_matrice(n, n)
    # Riempio la diagonale col valore 1
    for i in range(n):
        m[i][i] = 1
    return m

# Esercizio 5
# Questa versione si basa sulla funzione ausiliaria crea_matrice.
def tavola_pitagorica(n):
    # Creo una matrice piena di 0
    m = crea_matrice(n, n)
    # La riempio con i valori corretti
    for num_riga in range(n):
        for num_colonna in range(n):
            m[num_riga][num_colonna] = num_riga * num_colonna
    return m

# Esercizio 4
# Questa versione crea direttamente il risultato voluto senza passare
# per la matrice nulla e senza utilizzare la funzione crea_matrice.
def matrice_identica_bis(n):
    # La variabile risultato conterrà la matrice ovvero una lista di righe
    risultato = []
    for num_riga in range(n):
        # Nella variabile riga verrà accumulata la riga di indice `num_riga`.
        # Viene inizializzata alla lista vuota, e riempita gradatamente
        riga = []
        for num_colonna in range(n):
            riga.append(1 if num_riga == num_colonna else 0)
        risultato.append(riga)
    return risultato

# Esercizio 5
# Questa versione crea direttamente il risultato voluto senza passare
# per la matrice nulla e senza utilizzare la funzione crea_matrice.
def tavola_pitagorica_bis(n):
    # Simile a matrice_identica_bis, cambia solo il modo di riempire la matrice.
    risultato = []
    for num_riga in range(n):
        riga = []
        for num_colonna in range(n):
            # questa è l'unica riga di differenza con matrice_identica_bis
            riga.append(num_riga * num_colonna)
        risultato.append(riga)
    return risultato

# Esercizio 6
# Se le matrici a e b fossero rettangolari, potremmo usare la funzione
# crea_matrice per creare la matrice risultato e poi riempirla con  i
# valori corretti. Ma se non è regolare, dobbiamo creare la matrice
# risultato mano a mano che ne calcoliamo i valori.
def somma_matrici2(a, b):
    # Lo schema è molto simile a matrice_identica_bis e tavola_pitagorica_bis,
    # ma il numero di righe e di colonne viene dedotto dalla matrice `a` invece
    # che da un parametro in ingresso.
    risultato = []
    # Il numero di righe del risultato è uguale al numero di righe di `a`
    for num_riga in range(len(a)):
        riga = []
        # Il numero di colonne risultato della riga `num_riga` è uguale al numero di colonne
        # della riga `num_riga` nella matrice `a`.
        for num_colonna in range(len(a[num_riga])):
            riga.append(a[num_riga][num_colonna] + b[num_riga][num_colonna])
        risultato.append(riga)
    return risultato
