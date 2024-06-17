from random import random

TRIES = 10000

hits = 0
for i in range(TRIES) :
    r = random() # ritorna un valore randomico presente in un intervallo tra 0 e 1 dove solo l'intervallo sinistro è incluso
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r

    if x * x + y * y <= 1 :
        hits += 1

pi_estimate = 4.0 * hits / TRIES
print("Estimate for pi: ", pi_estimate)