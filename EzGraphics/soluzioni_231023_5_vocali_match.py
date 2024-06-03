parola = input("Immetti parola: ")
pos = int(input("Immetti posizione: "))
match parola[pos]:
    case "a" | "e" | "i" | "o" | "u":
        print("vocale")
    case _:
        print("consonante")
