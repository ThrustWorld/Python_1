# Programma che legge una stringa e ne visualizza il primo carattere, l'ultimo e il carattere centrale.
# Se il numero di caratteri della stringa è pari, visualizza il primo dei due caratteri centrali.

stringa = input("Immetti una stringa: ")
print("Il primo carattere è", stringa[0])
# Bisogna calcolare qual'è la posizione centrale. Facendo alcuni esperimenti a mano, si vede che la
# formula che funziona sia nel caso di stringhe di lunghezze pari che nel caso di stringhe di
# lunghezza dispari è la seguente.
posizione_centrale = (len(stringa) - 1) // 2
print("Il caratere centrale è", stringa[posizione_centrale])
print("L'ultimo carattere è", stringa[-1]) # in alternativa, posso mettere len(stringa)-1 al posto di -1