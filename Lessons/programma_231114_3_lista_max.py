# inizializzata a 0, conterrà il massimo dei valori inseriti
massimo = 0
#  questa variabile conterrà la lista dei valori inseriti
lista_elementi_inseriti = [ ]

while True:
    n = int(input("Immetti valore: "))
    # se il numero immesso è negativo, esco dal ciclo
    if n < 0:
        break
    # se il numero immesso è maggiore del massimo, aggiorna il massimo
    if n > massimo:
        massimo = n
    # aggiungi il numero immesso alla lista dei valori
    lista_elementi_inseriti.append(n)
    #print("La lista contiene",lista_elementi_inseriti)

# scorre la lista dei valori inseriti
for i in lista_elementi_inseriti:
    if i == massimo:
        # se il valore corrente è il massimo, lo stampa evidenziato
        print(i, "<=== MASSIMO")
    else:
        # altrimenti lo stampa normale
        print(i)
