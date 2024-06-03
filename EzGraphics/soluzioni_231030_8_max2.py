import sys

# Questa versione non assume che l'utente inserisca sicuramente il primo
# numero. Questa parte iniziale legge quindi l'input, ma termine se l'utente
# non inserisce nulla.
input_str = input("Immetti un numero: ")
if input_str == "":
    sys.exit("Non hai inserito nessun numero")
max_value = int(input_str)

# Da questo punto in poi è simile alla versione precedente.
input_str = input("Immetti un numero: ")
while input_str != "":
    n = int(input_str)
    if n > max_value:
        max_value = n
    input_str = input("Immetti un numero: ")
print("Il valore massimo è", max_value)
