MEDALS = 3
COUNTRIES = 7

countries = ["Canada", "China", "Germany", "Korea", "Japan", "Russia", "United States"]

counts = [    # Matrice definita
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 1],
    [1, 1, 0]
]

print("        Country    Gold    Silver    Bronze    Total")

# Accesso agli elementi della tabella
for i in range(COUNTRIES) : # i = righe
    total = 0
    print("%15s" % countries[i], end="")
    for j in range(MEDALS) : # j = colonne
        print("%8d" % counts[i][j], end="")
        total = total + counts[i][j]

    print("%8d" % total)