from random import randint

# In questo file trovate tutte le soluzioni agli esercizi del 20 novembre 2023

# Esercizio 1
def cerca_positivo(l):
    for v in l:
        if v >= 0:
            return v
    return -1

# Esercizio 2
def cerca_positivo_pos(l):
    for i in range(len(l)):
        if l[i] >= 0:
            return i
    return -1

# Esercizio 3
def count(l, x):
    counter = 0
    for v in l:
        if v == x:
            counter += 1
    return counter

# Esercizio 4
def sum_list(l1, l2):
    # Creiamo sin dall'inizio una lista della lunghezza giusta
    l = [0] * len(l1)
    # Usiamo un solo indice che serve a scandire sia gli elementi di l1 che di l2
    for i in range(len(l1)):
        # Metto nella posizione i-esima di l la somma dei valori corrispondenti in l1 ed l2
        l[i] = l1[i] + l2[i]
    return l

# Esercizio 4 soluzione alternativa
def sum_list_2(l1, l2):
    # Partiamo da una lista vuota
    l = []
    # Usiamo un solo indice che serve a scandire sia gli elementi di l1 che di l2
    for i in range(len(l1)):
        # Aggiungo ad l la somma degli elementi i-esimi di l1 ed l2
        l.append(l1[i] + l2[i])
    return l

# Esercizio 5
def input_list_int():
    l = []
    while True:
        s = input("Inserisci un numero: ")
        if s == "":
            break
        l.append(int(s))
    return l

# Esercizio 6
def random_list(n, k):
    l = [0] * n
    for i in range(n):
        l[i] = randint(1, k)
    return l
