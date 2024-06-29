"""
Propongo due possibili soluzioni di questo esercizio.

Il primo metodo usa le eccezioni: provo ad eseguire le operazioni di raddoppio,
ma se si verifica un errore catturo l'eccezione
e ripristino la matrice originale (che mi sono preventivamente salvato)

Il secondo metodo fa un controllo preventivo: se l non è abbastanza lungo o contiene
indici non validi, non fa nulla. Solo se l è corretta procede con l'operazione di
raddoppio.

Notare che le due soluzioni non fanno esattamente la stessa cosa. Nella prima soluzione
indici negativi possono essere validi (al solito, indicano una posizione a partire
dall'ultima) mentre nella seconda soluzione sono considerati errori.
"""


def copia_matrice(src):
    """
    Crea una copia della mtrice src e la restituisce (vedi test_es3.py per spiegazioni).
    """
    ris = []
    for i in range(len(src)):
        ris.append(src[i].copy())
    return ris


def raddoppia2(l, m):
    """
    Versione di raddoppia 2 con eccezioni.
    """
    # Creo una copia della matrice
    saved = copia_matrice(m)
    try:
        # Provo ad eseguire l'operazione
        for i in range(len(m)):
            m[i][l[i]] *= 2
    except IndexError:
        # Se si è verificato un errore, ricopio dentro m il vecchio contenuto, che avevo
        # precedentemente salvato in saved
        for i in range(len(saved)):
            for j in range(len(saved[i])):
                m[i][j] = saved[i][j]


def raddoppia2_bis(l, m):
    """
    Versione di raddoppia 2 con controllo preventivo.
    """
    # Se l non è abbastanza lungo, esci senza fare nulla
    if len(l) < len(m):
        return
    # Se l contiene elementi che non sono indici validi per le righe di m, esci senza fare nulla
    for i in range(len(m)):
        col = l[i]
        if col < 0 or col >= len(m[i]):
            return
    # Se siamo arrivati a questo punto vuol dire che è tutto a posto e possiamo procedere.
    for i in range(len(m)):
        m[i][l[i]] *= 2


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
raddoppia2_bis([1, 4, 0], m)
print(m)
