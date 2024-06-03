# Importo la funzione

from programma_231114_1_mymodule import somma_numeri

n1 = int(input("Immetti primo numero: "))
n2 = int(input("Immetti secondo numeri: "))
somma = somma_numeri(n1, n2)
print(f"La somma dei numeri compresi tra {n1} e {n2} è {somma}")
