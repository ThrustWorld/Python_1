def area_trapezio(b1, b2, h):
    """
    Calcola l'area di un trapezio di basi 'b1' e 'b2' e di altezza 'h'.
    """
    # si potrebbe anche assegnare il risultato di (b1+b2)*h ad una variabile
    # area e restituire quest'ultima, ma non è necessario: l'istruzione return
    # può prendere direttamente una espressione coe valore da restituire
    return (b1 + b2)*h / 2

print("L'area di un trapezio di basi 2 e 5 ed altezza 3 è", area_trapezio(2, 5, 3))