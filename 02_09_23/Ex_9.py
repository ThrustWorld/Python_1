print("Conversione x minuti in y ore")

minuti = int(input("Tempo espresso in minuti :"))

ore = minuti // 60
ore_resto = minuti % 60

ora_e = " "
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
print(ore, ora_e, ore_resto, minuto_i)