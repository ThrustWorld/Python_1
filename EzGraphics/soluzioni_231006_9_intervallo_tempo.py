    # Si scriva un programma che prende in input un periodo di tempo espresso in minuti, e
    # calcola l'equivalente in ore. Ad esempio, con input 80 restituisce "1 ora e 20 minuti".
    # Ignorare per ora i problemi relativi alla sintassi della lingua italiana (vanno bene
    # anche output del tipo "2 ora e 30 minuti").

    # notare l'uso di una costante per il "numero magico" 60
    MINUTI_PER_ORA = 60

    tempo = int(input("Immetti periodo di tempo in minuti: "))
    ore = tempo // MINUTI_PER_ORA
    minuti = tempo % MINUTI_PER_ORA
    print(ore, "ore e", minuti, "minuti")
