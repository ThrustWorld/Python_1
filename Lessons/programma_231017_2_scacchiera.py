# Esercizio R3.9 (modificato)
#
# Si scriva un programma che prende in input la coordinata di una cella della
# scacchiera, nella notazione <lettera><numero> (ad esempio g3), e visualizzi
# il colore della cella. Prendere il seguente pseudo-codice come esempio:
#
# se la lettere è a, c, e oppure g
#   se il numero è dispari
#      colore = nero
#   altrimenti
#      colore = bianco
# altrimenti
#    se il numero è dispari
#       colore = bianco
#     altrimenti
#        colore= nero

coordinate = input("Immetti coordinate casella: ")

colonna = coordinate[0]    # estra colonna (lettera)
riga = int(coordinate[1])  # estra riga (numero) e la converte in intero

if colonna in "aceg":  # controlla se colonna è uno tra a, c, e oppure g
    if riga % 2 == 1:
        colore = "nero"
    else:
        colore = "bianco"
else:
    if riga % 2 == 1:
        colore = "bianco"
    else:
        colore = "nero"

print("Il colore dela casella è", colore)