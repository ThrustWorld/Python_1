# Esercizio: Conversione di minuti in ore
print("Conversione x minuti in y ore")

minuti = int(input("Tempo espresso in minuti :"))

ore = minuti // 60 # / = ritorna una divisione con quoziente + resto; // = solo quoziente # % = solo resto  
ore_resto = minuti % 60 # Sempre grazie a Google sappiamo come si convertono i minuti in ore

ora_e = " "

#OFF_TOPIC: "if" e "elif" non le ha ancora spiegate. In breve, si chiamano strutture di controllo e accettano una condizione rispondendo
# alla domanada Vero o Falso. Esempio: Se il valore di ore è 1 allora ore > 1 è falso e quindi esegue l'istruzione perchè ore è = 1,
# la condizione è soddisfatta. (== -> comparazione tra valori di variabili)
if ore > 1:
    ora_e = "ore e "
elif ore == 1:
    ora_e = "ora e "

minuto_i = " "
if ore_resto > 1:
    minuto_i = "minuti"
elif ore_resto == 1:
    minuto_i = "minuto"

print("Conversione in ore:")
print(ore, ora_e, ore_resto, minuto_i) # Come vedi "print()" può prendere più variabili al suo interno. Le variabili all'interno
# di "()" prendono il nome di "argomenti"