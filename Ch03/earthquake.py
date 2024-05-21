richter = float(input("Magnitude on the Richter scale: "))

if richter >= 8.0 :
    print("Most structure fail")
elif richter >= 7.0 :   # Il costrutto elif sostituisce i "nested if" migliorando la lettura del codice
    print("Many buildings destroyed")
elif richter >= 6.0 :
    print("Many buildings considerably damaged, some collapse")
elif richter >= 4.5 :
    print("Damage to poorly constructed buildings")
else :
    print ("No destruction of buildings")