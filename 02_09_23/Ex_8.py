#Calcolare l'area di un trapezio


print("Calcolo area di un trapezio.") # Stringa in output (Nel terminale che si apre quando avvii il programma leggerai "Calcolo area
# di un trapezio")
print("Compilare i seguenti campi:") # Stringa in output
base_minore = float(input("- Base minore: ")) # Questo comando "type(input(""))" serve per poter scrivere un valore attraverso il terminale
# Come abbiamo visto ci sono diversi tipi(int, float, char, ...). "base_minore" è una variabile. Dopo = rappresenta il valore assegnato
# alla variabile
base__maggiore = float(input("- Base maggiore: ")) # Stessa cosa di sopra
altezza = float(input("- Altezza: ")) 
area = (base_minore + base__maggiore) * altezza // 2 # / = ritorna una divisione con quoziente + resto; // = solo quoziente 
# % = solo resto  # Grazie a Google sappiamo come si calcola l'area di un trapezio
print(area) # E' lo stesso comando print("Quello che ti pare"). Accetta anche le variabili(senza "") e le converte automaticamente in base al tipo