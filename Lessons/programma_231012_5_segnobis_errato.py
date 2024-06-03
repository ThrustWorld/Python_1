# Programma che prende in input un numero intero e stampa se è positivo,
# negativo o nullo.

# Versione senza if annidati ma sbagliata

numero = int(input("Immetti un numero: "))
if numero > 0:
    print("positivo")
if numero == 0:
    print("zero")
else:
    print("negativo")

# Rispetto alla versione precedente abbiamo rimpiazzato l'istruzione
# `if numero < 0` con una clausola else. Il programma non funziona bene.
# Se il numero immess è positivo, prima viene stampato `positivo``, ma
# poiché la condizione alla riga 9 `numero==0` è falsa, viene eseguito
# il ramo else e quindi viene stampato anche `negativo`.