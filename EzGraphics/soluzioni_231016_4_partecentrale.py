"""
Scrivere un programma che accetta una stringa in input e stampa:
  * il carattere centrale, se la lunghezza della stringa è dispari;
  * i due caratteri centrali, se la lunghezza della stringa è pari.
"""

stringa = input("Immetti una stringa: ")
# controllo se la lunghezza della stringa è pari o dispari
if len(stringa) % 2 == 0:
    # se l'esecuzione passa pper qui, vuol dire che lunghezza pari
    pos = len(stringa) // 2 - 1  # primo carattere da estrarre
    # estra il caratter in posizione pos e il successivo
    # quello in posizione pos+2 non lo estrae perché l'estremo destro è escluso
    estrazione = stringa[pos:pos+2]
else:
    # carattere in posizione centrale
    pos = (len(stringa) - 1)  // 2
    # estraggo il carattere in quella posizione
    estrazione = stringa[pos]
print("La parte centrale della stringa è:", estrazione)
