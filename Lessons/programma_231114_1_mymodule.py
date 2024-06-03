"""
Questo modulo di esempio contiene esclusivamente la funzione somma_numeri.
"""

def somma_numeri(a, b):
    """
    Dati 'a' e 'b' numeri interi, restituisce la somma di tutti i numeri interi compresi tra di essi
    (estremi inclusi).
    """
    somma = 0
    for i in range(a, b+1):
        somma += i
    return somma
