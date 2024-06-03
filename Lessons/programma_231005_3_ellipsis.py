"""
Esercizio P2.22 del libro di testo

Programma che prende in input una stringa, e ne visualizza i primi 3 caratteri, seguiti da tre punti, seguiti dagli ultimi 3
caratteri.
"""

stringa = input("Immetti una stringa: ")

primo_pezzo = stringa[0:3]
# Usare "." * 3 per creare una stringa di tre puntini non è particolarmente
# leggibile, sarebbe meglios scrivere direttamente "...", ma è stato fatto
# per ripassare la funzionalità di ripetizione di Python
pezzo_centrale = "." * 3
pezzo_finale = stringa[-3:]
risultato = primo_pezzo + pezzo_centrale + pezzo_finale

# In alternativa, possiamo rimpiazzare le righe da 10 a 16 con l'unica
# riga che segue: non serve creare tutte questi variabili per i risultati
# intermedi.
# risultato = stringa[0:3] + ("." * 39) + stringa[-3:]

print(risultato)
