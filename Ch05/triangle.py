def main():
    print_triangle(4)

def print_triangle(length):
    if length < 1 : return # le istruzioni singole possono essere messe su un'unica riga
    print_triangle(length - 1) # Ricorsione, ripetizione della funzione all'interno di se stessa
    print("[]" * length)

main()