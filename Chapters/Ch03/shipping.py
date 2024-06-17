country = input("Country: ")
state = input ("State: ")

shipping_cost = 0.0

if country == "USA" :
    if state == "AK" or state == "HI" : # Operatore "or" unisce più condizioni e basta che una sia valida per far sì che la condizione sia vera
        shipping_cost = 10.0
    else :
        shipping_cost = 5.0
else :
    shipping_cost = 10.0

print("Shipping cost to %s, %s: %.2f" %(country, state, shipping_cost))