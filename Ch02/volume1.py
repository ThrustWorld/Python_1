##
# Questo programma calcola il volume in litri di una confezione di bibite con sei lattine, seguito dal volume di una tale confezione
# insieme a una bottiglia da due litri

# Litri in una lattina da 12 once e in una bottiglia da due litri
CAN_VOLUME = 0.355          # Costante
BOTTLE_VOLUME = 2

# Numero di lattine in una confezione
cans_per_pack = 6

# Volume totale nelle lattine di una confezione
total_volume = cans_per_pack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", total_volume, "liters")

# Volume totale di una confezione e di una bottiglia
total_volume = total_volume + BOTTLE_VOLUME
print("A six-pack and a two-liter bottle contain", total_volume, "liters")