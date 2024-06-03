# La variabile max_value contiene il massimo corrente. Non è possibile però
# inizializzarla ad un valore costante, perché qualunque valore iniziale
# potrebbe essere sbagliato. Pertanto, la inizializzo con il primo valore in
# input (uso l'assunzione che l'utente immetta almeno un valore)
max_value = int(input("Immetti un numero: "))
input_str = input("Immetti un numero: ")
while input_str != "":
    n = int(input_str)
    # Se l'utente ha immesso un valore più grande del massimo corrente, aggiorno
    # il massimo corrente.
    if n > max_value:
        max_value = n
    input_str = input("Immetti un numero: ")
print("Il valore massimo è", max_value)
