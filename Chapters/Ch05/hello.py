def box_string(contents):
    n = len(contents)
    print("-" * (n + 2))
    print("!" + contents + "!")
    print("-" * (n + 2))

box_string("Hello") # Invocazione di una funzione che non deve restituire un valore