temp = input("Immetti temperatura in Celsius o Farehneit: ")
# Il metodo strip rimuove gli spazi all'inizio e alla fine. Come il metodo upper,
# non modifica la stringa originale, ma restituisce una nuova stringa che posso
# assegnare ad una variabile, eventualmente quella originaria.
temp = temp.strip()
# estrae ultimo carattere
standard = temp[-1]
# estrae tutti i caratteri tranne l'ultimo (ricordate che l'estremo destro non è incluso)
# e converte nello stesso tempo in float
temp = float(temp[:-1])
match standard:
  case "c" | "C":
    fahreneit = 9 * temp / 5 + 32
    # uso le f-stringhe senza specificare la dimensione in spazi dell'output ma
    # solo il numero di cifre dopo la virgola
    print(f"La temperatura in gradi Fahreneit è {fahreneit:.1f}")
  case "f" | "F":
    celsius = 5 *(temp - 32)/9
    print(f"La temperatura in gradi Celsius è {celsius:.1f}")
  case _:
    print("Unità di misura non valida")
