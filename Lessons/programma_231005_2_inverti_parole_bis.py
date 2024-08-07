"""
Programma che prende in input (da tastiera) una frase e stampa la stessa frase in cui però la prima parola viene spostata alla fine.

Ad esempio: se l'utente immette "Ciao sono Gianluca", lui stampa "sono Gianluca Ciao".

Questo variante, suggerita da uno studente, risovle il problema delle stringhe immesse dall'utente senza
spazio aggiungendone forzatamente uno.
"""

# PUNTO 1: chiedere l'input

# Aggiungo uno spazio alla fine: in questo modo siamo sicuri che la stringa
# frase avrà almeno uno spazio.

frase = input("Immetti frase: ") + " "

# PUNTO 2: calcolare la stringa da stampare

# PUNTO 2.1: trovare la posizione del primo spazio
posizione_primo_spazio = frase.find(" ")

# PUNTO 2.2: estrarre la prima parola e la parte restante
prima_parola = frase[0:posizione_primo_spazio]
frase_restante = frase[posizione_primo_spazio+1:]

# PUNTO 2.3: concatenare i due pezzi estratti

# Non metto più uno spazio tra frase_restate e prima_parola, perché c'è già lo spazio
# inserito alla riga 16.

risultato = frase_restante + prima_parola

# PUNTO 3: stampare la stringa determinata al punto 2
print("*"+risultato+"*")
