# Simulazione pannello ascensore che salta il piano numero 13

# Acquisizione piano
floor = int(input("Floor: "))

# Correzione piano se 13 o maggiore
if floor > 13 :
    actual_floor = floor - 1 # Oppure si usa l'operatore condizionale -> actualFloor = floor - 1 if floor > 13 else actualFloor = floor
else :
    actual_floor = floor

print("Actual floor: ", actual_floor)