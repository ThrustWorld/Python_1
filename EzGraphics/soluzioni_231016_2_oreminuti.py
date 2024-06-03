"""
Modificare il programma che risolve l'Esercizio 9 della Lezione laboratorio
del 2/10/2023 per visualizzare un messaggio di errore nel caso l'input
inserito dall'utente è negativo.
"""

# notare l'uso di una costante per il "numero magico" 60
MINUTI_PER_ORA = 60

tempo = int(input("Immetti periodo di tempo in minuti: "))
if tempo < 0:
    print("Il valore input non può essere negativo")
else:
    ore = tempo // MINUTI_PER_ORA
    minuti = tempo % MINUTI_PER_ORA
    print(ore, "ore e", minuti, "minuti")
