somma = 0
# Preparo la variabile `continuare` col valore "S" in modo da entrare
# la prima volta nel ciclo while.
continuare = "S"
while continuare == "S":
    n = int(input("Inserisci un numero: "))
    somma += n
    continuare = input("Vuoi inserire un altro numero? (S / N): ")
print("La somma dei numeri inseriti è", somma)
