# Esercizio 0
def somma_numeri(n):
    # Notare che è possibile inserire una istruzione dopo i due punti senza
    # andare a capo. Si può usare solo per suite costituite da una singola istruzione.
    if n == 0: return 0
    return n + somma_numeri(n-1)

# Esercizio 1
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

# Esercizio 2
def reverse(text):
    if text == "": return "" # caso base
    else: return reverse(text[1:]) + text[0]

# Esercizio 3
def reverse_sub(text, n):
    if n >= len(text): return "" # caso base
    else: return reverse_sub(text, n+1) + text[n]

def reverse_bis(text):
    return reverse_sub(text, 0)

# Esercizio 4
def reverse_iterativo(text):
    s = ""
    for c in text:
        s = c + s
    return s

# Esercizio 5
def substrings(s):
    if s == "": return [""]
    else:
        ris = []
        # determino tutte le sottostringhe che partono dal primo carattere
        for end in range(len(s)):
            ris.append(s[0:end+1])
        # aggiungo le sottostringhe della stringa s senza il promo carattere
        ris += substrings(s[1:])
        return ris

# Esercizio 5 versione iterativa
def substrings_iterative(s):
    ris = [""]
    # posizione iniziale della sottostringa
    for start in range(len(s)):
        # posizionme finale della sottostringa
        for end in range(start, len(s)):
            ris.append(s[start:end+1])
    return ris
