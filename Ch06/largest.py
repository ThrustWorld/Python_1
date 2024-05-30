values = []

user_input = input("Insert values or press Q to quit:")

while user_input.upper() != "Q" :
    values.append(float(user_input))
    user_input = input("Insert values or press Q to quit:")

# Massimo valore tra gli elementi della lista
largest = values[0]
for i in range(1, len(values)) :
    if values[i] > largest :
        largest = values[i]

# Ricerca lineare dell'elemento corrispondente al valore massimo
for element in values :
    if element == largest :
        print(element, "is the largest")