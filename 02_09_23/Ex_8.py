print("Calcolo area di un trapezio.")
print("Compilare i seguenti campi:")
base_minore = float(input("- Base minore: "))
base__maggiore = float(input("- Base maggiore: "))
altezza = float(input("- Altezza: "))
area = (base_minore + base__maggiore) * altezza // 2 # / = intero + resto; // = solo intero % = solo resto
print(area)