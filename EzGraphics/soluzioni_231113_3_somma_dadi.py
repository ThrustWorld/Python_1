from random import randint

def somma_dadi(n, k):
    """
    Genera `n` numeri interi casuali compresi tra 1 e 'k`, e restituisce la loro somma.
    """
    somma = 0
    for i in range(n):
        somma += randint(1, k)
    return somma

print(somma_dadi(3, 8))