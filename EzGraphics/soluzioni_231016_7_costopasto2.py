"""
Estendere il programma dell'Esercizio 5 in modo che particolari combinazioni
abbiano dei prezzi speciali:
  * menu (primo e secondo) € 6.50
  * menu completo (primo, secondo e contorno) € 8.00
"""

# costanti con i prezzi delle pietanze
PREZZO_PRIMO = 3.50
PREZZO_SECONDO = 4.00
PREZZO_CONTORNO = 2.50

# questa variabile conterrà il prezzo totale del menù
totale = 0.0

# chiede all'utente
domanda_primo = input("Hai mangiato il primo? ")
domanda_secondo = input("Hai mangiato il primo? ")
domanda_contorno = input("Hai mangiato il contorno? ")

if domanda_primo == "sì":
    # Considero prima il caso in cui il cliente mangia il primo, ed esamino
    # tutti i possobili casi (tre).
    if domanda_secondo == "sì":
        if domanda_contorno == "sì":
            totale = 8.00
        else:
            totale = 6.50
    else:
        totale = 3.50
else:
    # Se il cliente non ha mangiato il primo, non c'è nessun menù possibile
    # quindi procedo come per l'esercizio 5.
    if domanda_secondo == "sì":
        totale = totale + PREZZO_SECONDO
    if domanda_contorno == "sì":
        totale = totale + PREZZO_CONTORNO

print("Il pasto costa", totale, "€")
