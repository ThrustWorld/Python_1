# Esercizio P2.5 del libro di testo.

n1 = int(input("Imetti primo numero: "))
n2 = int(input("Immetti secondo numero: "))

# Si noti la necessità che tutte le etichette occupino lo stesso numero di
# caratteri. Qui la cosa è ottenuta aggiungendo manualmente il numero di
# spazi necessari.

print(f"Somma:        {n1+n2:10}")
print(f"Differenza:   {n1-n2:10}")
print(f"Prodotto:     {n1*n2:10}")
print(f"Valore medio: {(n1+n2)/2:13.2f}")
print(f"Distanza:     {abs(n1-n2):10}")
print(f"Massimo:      {max(n1,n2):10}")
print(f"Minimo:       {min(n1,n2):10}")
