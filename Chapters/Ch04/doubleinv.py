RATE = 5.0
INITIAL_BALANCE = 1000.0
TARGET = 2 * INITIAL_BALANCE

balance = INITIAL_BALANCE
year = 0

while balance < TARGET : # ciclo while, istruzioni eseguite finchè la condizione è rispettata
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest

print("The investment doubled after", year, "years")