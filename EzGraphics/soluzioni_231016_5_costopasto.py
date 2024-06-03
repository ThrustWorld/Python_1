"""
Scrivere un programma che calcola il prezzo di un pasto. Il programma chiede
all'utente le portate consumate con 3 domande ("Hai mangiato il primo?",
"Hai mangiato il secondo?", "Hai mangiato il contorno?") con possibili
risposte "sì" o "no". I prezzi applicati sono:
  * primo € 3.50
  * secondo € 4.00
  * contorno € 2.50
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

# Se l'utente ha mangiato il primo, incrementa la variabile totale
# con il costo del primo. Analogamente per secondo e contorno.
if domanda_primo == "sì":
    totale = totale + PREZZO_PRIMO
if domanda_secondo == "sì":
    totale = totale + PREZZO_SECONDO
if domanda_contorno == "sì":
    totale = totale + PREZZO_CONTORNO

print("Il pasto costa", totale, "€")
