import pytest
import random

from python.es3 import raddoppia

def test_1():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    l = [1, 2, 0]
    raddoppia(l, m)
    # Notare che l'istruzione assert confronta la matrice m (modificata dalla funzione raddoppia) con il
    # valore atteso. Una istruzione come
    #   assert raddoppia([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) ==  [[1, 4, 3], [8, 5, 6], [14, 8, 9]]
    # non funzionerebbe perché raddoppia non restituisce nulla (o, meglio, non avendo un return, restituisce
    # None, che non è certamente uguale alla matrice attesa)
    assert m == [[1, 4, 3], [4, 5, 12], [14, 8, 9]]

def copia_matrice(src):
    """
    Crea una copia della mtrice src e la restituisce.
    """
    # ris conterrà la matrice copia. Ricordiamo che una matrice è una lista di righe, quindi
    # inizialmente ris è una lista vuota.
    ris = []
    for i in range(len(src)):
        # per ogni riga di src, uso il metoo copy() per ottenere una copia della riga e la aggiungo
        # a ris con append
        ris.append(src[i].copy())
    # Notare che rimpiazzare le istruzioni di sopra con "ris = m.copy()"" non funziona, perché ris ed m sarebbero
    # due matrice diverse che hanno esattamente le stesse righe (non righe uguali, ma righe che puntano allo stesso oggetto).
    return ris


def test_2():
    # creo due matric 3x3 con tutti valori nulli
    m = [ [0,0,0], [0,0,0], [0,0,0] ]
    # la riempio con valori casuali
    for i in range(3):
        for j in range(3):
            m[i][j] = random.randint(1, 100)
    # copia la matrice m
    n = copia_matrice(m)
    # raddoppio i primo elemento di ogni riga di n
    for i in range(3):
        n[i][0] *= 2
    # eseguo la funzione raddoppia
    raddoppia([0, 0, 0], m)
    # se è tutto corretto, adesso le matrice m ed n dovrebbero essere uguali
    assert m == n
