# Simulazione pannello ascensore che salta il piano numero 13

# Acquisizione piano
floor = int(input("Floor: "))

# Correzione piano se 13 o maggiore
if floor > 13 :
    actualFloor = floor - 1 # Oppure si usa l'operatore condizionale -> actualFloor = floor - 1 if floor > 13 else actualFloor = floor
else :
    actualFloor = floor

print("Actual floor: ", actualFloor)