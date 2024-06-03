n = int(input("Immetti un numero: "))
# La variabile `duplicati` mantiene l'informazione se sono stati trovati
# duplicati o meno. Inizialmente è False, ma ad ogni iterazione si
# controlla la presenza di duplicati e, nel caso, si imposta a True.
duplicati = False
while n > 0:
    prec = n
    n = int(input("Immetti un numero: "))
    if n == prec:
        duplicati = True

# Notare che la condizione è semplicemente `duplicati` e non `duplicati==True`
# in quanto duplicati è gia una variabile booleana, non c'è motivo di
# confrontarla con True.
if duplicati:
    print("Ci sono duplicati")
else:
    print("Non ci sono duplicati")
