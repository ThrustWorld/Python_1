# questa volta importo la sola funzione exit invece che tutto il modulo sys
from sys import exit

n = int(input("Inserisci valore numerico mese: "))

match n:
    case 1:
        mese = "gennaio"
    case 2:
        mese = "febbraio"
    case 3:
        mese = "marzo"
    case 4:
        mese = "aprile"
    case 5:
        mese = "maggio"
    case 6:
        mese = "giugno"
    case 7:
        mese = "luglio"
    case 8:
        mese = "agosto"
    case 9:
        mese = "settembre"
    case 10:
        mese = "ottobre"
    case 11:
        mese = "novembre"
    case 12:
        mese = "dicembre"
    case _:
        exit("Valore non valido")

print("Il mese scelto è", mese)
