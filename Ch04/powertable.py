N_MAX = 4
X_MAX = 10

for n in range(1, N_MAX + 1) :
    print("%10d" % n, end="")

print()
for n in range(1, N_MAX + 1) :
    print("%10s" % "x", end="")

print("\n", "    ", "-" * 35)

for x in range(1, X_MAX + 1) : # nested loops, matrice
    for n in range(1, N_MAX + 1) :
        print("%10.0f" % x ** n, end="")
    print()