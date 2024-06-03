import sys

MINUTI_PER_ORA = 60

tempo = int(input("Immetti periodo di tempo in minuti: "))
if tempo < 0:
    sys.exit("Il valore input non può essere negativo")

ore = tempo // MINUTI_PER_ORA
minuti = tempo % MINUTI_PER_ORA
parola_ore = "ora" if ore == 1 else "ore"
parola_minuti = "minuto" if minuti == 1 else "minuti"

print(ore, parola_ore, "e", minuti, parola_minuti)
