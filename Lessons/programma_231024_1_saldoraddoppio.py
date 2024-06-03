saldo = float(input("Immetti saldo iniziale: "))
tasso = float(input("Tasso di interesse: "))
limite = 2 * saldo
anno = 0

while saldo < limite:
    anno += 1
    interesse = saldo * tasso / 100
    saldo += interesse

print("Per raddoppiare il capitale servono", anno, "anni")
