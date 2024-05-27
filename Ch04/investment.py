RATE = 5.0
INITIAL_BALANCE = 10000.0

num_years = int(input("Enter number of years: "))

balance = INITIAL_BALANCE
for year in range(1, num_years + 1) : # Iterazione basata su un intervallo di numeri, minimo incluso e massimo escluso
    interest = balance * RATE / 100
    balance += interest
    print("%4d %10.2f" % (year, balance))