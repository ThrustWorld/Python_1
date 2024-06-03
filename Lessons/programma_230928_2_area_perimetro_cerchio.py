# Utilizzo la funzione input per chiedere all'utente il valore del ragigo
raggio = int(input("Immetti il raggio del cerchio: "))
# Metto il valore 3.1415 (approssimazione di pigreco) nella variabile PIGRECO, in modo da non
# avere "numeri magici" dentro il programma. Per convenzione, per i valori costanti si preferisce
# usare variabili scritte tutte in lettere maiuscole.
PIGRECO = 3.1415
area = PIGRECO * raggio * raggio
perimetro = 2 * PIGRECO * raggio
print("L'area del cerchio è", area)
print("Il perimetro del cerchio è", perimetro)