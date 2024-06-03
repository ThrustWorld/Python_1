"""
Modificare il programma dell'esercizio 2 per far sì che la parole "ore"
e "minuti" siano correttamente declinate al singolare quando necessario.
In altre parole, se l'input è 65, l'output deve essere "1 ora e 5 minuti",
non "1 ore e 5 minuti".

In questo programma, uso una variabile stringa parola_ora che inizializzo
a "ore" o ad "ora" a seconda di come è corretto dal pusto di vista grammaticale.
Cosa analoga con una variabile parola_minuti per i minuti. Poi utilizzo
queste variabili al posto delle stringhe "ore" e "minuti" della precedente
versione. In questo modo me la cavo con solo due if.
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
        parola_ore = "ora"
    else:
        parola_ore = "ore"

    if minuti == 1:
        parola_minuti = "minuto"
    else:
        parola_minuti = "minuti"

    print(ore, parola_ore, "e", minuti, parola_minuti)
