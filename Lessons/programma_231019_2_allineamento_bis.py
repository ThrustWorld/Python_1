# Esercizio P2.5 del libro di testo.

# Versione che usa la specifica di formato per far sì che tutte le etichette
# occupino lo stesso numero di caratteri.
#
# Messo solo come esempio, la versione originale è più leggibile.

n1 = int(input("Imetti primo numero: "))
n2 = int(input("Immetti secondo numero: "))

print(f"{'Somma':14} {n1+n2:10}")
print(f"{'Differenza':14} {n1-n2:10}")
print(f"{'Prodotto':14} {n1*n2:10}")
print(f"{'Valore medio':14} {(n1+n2)/2:13.2f}")
print(f"{'Distanza':14} {abs(n1-n2):10}")
print(f"{'Massimo':14} {max(n1,n2):10}")
print(f"{'Minimo':14} {min(n1,n2):10}")
