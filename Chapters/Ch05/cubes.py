def main() : # sintassi funzione senza parametri
    result1 = cube_volume(2) # invocazione della funzione
    result2 = cube_volume(10)
    print("Result 1: ", result1)
    print("Result 2: ", result2)

def cube_volume(side_length) : # sintassi funzione con parametri
    volume = side_length ** 3
    return volume # risultato da restituire

main()