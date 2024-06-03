s = input("Immetti stringa: ")
# esamina tutti i caratteri di c
for c in s:
    # il metodo isspace() restituisce True se il carattere a cui è
    # applicato è uno spazio
    if c.isspace():
        # se c è uno spazio, lo stampo
        print(c, end="")
    else:
        # altrimento stampo un asterisco
        print("*", end="")
# alla fine vado a capo
print()