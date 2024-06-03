"""
Modificare il programma dell'esercizio 2 per far sì che la parole "ore"
e "minuti" siano correttamente declinate al singolare quando necessario.
In altre parole, se l'input è 65, l'output deve essere "1 ora e 5 minuti",
non "1 ore e 5 minuti".

In questa versione evito l'uso di variabili ausiliarie parola_ore e
parola_minuti, ma devo considerare tutte le possibile combinazioni
tra l'uso di ora/ore e minuto/minuti.
"""

# notare l'uso di una costante per il "numero magico" 60
MINUTI_PER_ORA = 60

tempo = int(input("Immetti periodo di tempo in minuti: "))
if tempo < 0:
    print("Il valore input non può essere negativo")
else:
    ore = tempo // MINUTI_PER_ORA
    minuti = tempo % MINUTI_PER_ORA
    if ore == 1:
        if minuti == 1:
            print(ore, "ora e", minuti, "minuto")
        else:
            print(ore, "ora e", minuti, "minuti")
    else:
        if minuti == 1:
            print(ore, "ore e", minuti, "minuto")
        else:
            print(ore, "ore e", minuti, "minuti")
