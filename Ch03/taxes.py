RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0

income = float(input("Income: "))
status = input("S for single and M for married: ")

tax1 = 0.0
tax2 = 0.0

if status == "S" :
    if income <= RATE1_SINGLE_LIMIT :       # Nested -> Annidazione di enunciato, if dentro if
        tax1 = RATE1 * income
    else :
        tax1 = RATE1 * RATE1_SINGLE_LIMIT
        tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)
else :
    if income <= RATE1_MARRIED_LIMIT :
        tax1 = RATE1 * income
    else :
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)

totalTax = tax1 + tax2

print("Total: %.2f" % totalTax)