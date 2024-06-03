# In questo programma quello che normalmente è il programma principale è stato
# spostato nella funzione main, e il programma principale si limita a chiamare
# questa funzione.

def area_trapezio(b1, b2, h):
    """
    Calcola l'area di un trapezio di basi 'b1' e 'b2' e di altezza 'h'.
    """
    # si potrebbe anche assegnare il risultato di (b1+b2)*h ad una variabile
    # area e restituire quest'ultima, ma non è necessario: l'istruzione return
    # può prendere direttamente una espressione coe valore da restituire
    return (b1 + b2)*h / 2

def main():
    base1 = int(input("Immetti base minore del trapezio: "))
    base2 = int(input("Immetti base maggiore del trapezio: "))
    altezza = int(input("Imetti altezza del trapezio: "))
    print("L'area del trapezio è", area_trapezio(base1, base2, altezza))

main()
