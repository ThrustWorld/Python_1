"""
Scrivere un programma per il gioco della morra cinese (carta-forbici-sasso).
Il programma chiede all'utente la scelta dei due giocatori, che deve
essere in entrambi i casi una lettera tra C, F o S. Il programma poi
comunica il vincitore e il criterio per determinatre il vincitore. Il programma
dovrà consentire ai giocatori di digitare lettere maiuscole o minuscole.
"""

# Costanti con i messaggi da visualizzare

VINCE = "Vince giocartore"
PAREGGIO = "Pareggio"
MOTIVAZIONE_F_C = ": le forbici tagliano la carta"
MOTIVAZIONE_C_S = ": la carta avvolge il sasso"
MOTIVAZIONE_S_F = ": il sasso spunta le forbici"


giocatore1 = input("Scelta giocatore 1 (C, F o S): ").upper()
giocatore2 = input("Scelta giocatore 2 (C, F o S): ").upper()

# Nelle righe qui sopra uso il metodo upper() per convertire in maiuscolo l'input.
# Upper è stato messo nella stessa espressione di input, ma è possibile farlo in
# una riga separa, ad esempio:
#
# giocatore1 = input("Scelta giocatore 1 (C, F o S): ")
# giocatore1 = giocatore1.upper()
#
# È importante comunque ricordare che il metodo upper() non modifica la stringa a cui
# è applicato, ma produce un risultato che devo assenare ad una variabile (o usare
# in altro modo). È esattamente la stessa motivazione per cui se voglio sommare 2
# alla variabile x, posso scrivere solo "x + 2" ma devoscrivere "x = x + 2".

if giocatore1 == "C":
    if giocatore2 == "S":
        print(VINCE, 1, MOTIVAZIONE_C_S)
    if giocatore2 == "F":
        print(VINCE, 2, MOTIVAZIONE_F_C)
    if giocatore2 == "C":
        print(PAREGGIO)

if giocatore1 == "F":
    if giocatore2 == "C":
        print(VINCE, 1, MOTIVAZIONE_F_C)
    if giocatore2 == "F":
        print(PAREGGIO)
    if giocatore2 == "S":
        print(VINCE, 2, MOTIVAZIONE_S_F)

if giocatore1 == "S":
    if giocatore2 == "C":
        print(VINCE, 2, MOTIVAZIONE_F_C)
    if giocatore2 == "F":
        print(VINCE, 1, MOTIVAZIONE_S_F)
    if giocatore2 == "S":
        print(PAREGGIO)
