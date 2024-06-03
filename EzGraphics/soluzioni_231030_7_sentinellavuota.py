somma = 0
# Uso input senza nessuna conversione. In questo modo non si verificano errori
# se l'utente immette una stringa vuota, cosa che posso controllare come
# condizione di ingresso al ciclo while.
input_str = input("Immetti un numero: ")
while input_str != "":
    # Quando mi serve il valore inserito sotto forma di numero, lo converto
    # con la funzione int.
    n = int(input_str)
    somma += n
    input_str = input("Immetti un numero: ")
print("La somma dei numeri inseriti è", somma)
