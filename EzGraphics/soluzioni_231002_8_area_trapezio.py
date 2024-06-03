# Scrivere un programma Python che calcola l'area di un trapezio. Il programma deve prendere in input
# i tre parametri richiesti (base binore, base maggiore, altezza) e stampare l'area, corredando il
# tutto di scritte appropriato che fatto capire all'utente del programma quello che sta succedendo.

base_minore = float(input("Immettere base minore: "))
base_maggiore = float(input("Immettere base maggiore: "))
altezza = float(input("Immettere altezza: "))
area = (base_minore + base_maggiore) * altezza / 2
print("L'area è", area)