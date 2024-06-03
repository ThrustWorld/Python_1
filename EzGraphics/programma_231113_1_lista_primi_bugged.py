def primelist(n):
    """
    Stampa la lista di tutti i numeri primi fino ad n.
    """
    i = 1
    while i <= n:
        if isprime(i):
            print(i)
        i += 2

def isprime(n):
    """
    Restituisce True se n è primo, False altrimenti.
    """
    if n == 2:
        # 2 è primo
        return True

    if n % 2 == 0:
        # Nessun altro numero pari è primo
        return False

    k = 3  # Non serve dividere per 2 perché n è dispari
    # è sufficiente provare, come divisori, i numeri fino a sqrt(n)
    while k * k < n:
        if n % k == 0:
            # non è primo perché è divisibile per k
            return False
        k = k + 2

    return True

n = int(input("Immetti limite superiore sequenza: "))
primelist(n)