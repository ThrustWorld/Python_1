parola = input("Immetti parola: ")
pos = int(input("Immetti posizione: "))
if parola[pos] in "aeiou":
    print("vocale")
else:
    print("consonante")