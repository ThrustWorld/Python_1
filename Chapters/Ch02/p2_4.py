number_x = int(input("Digita un primo numero: "))
number_y = int(input("Digita un secondo numero: "))

sum = number_x + number_y
difference = number_x - number_y
product = number_x * number_y
average_value = sum / 2
distance = abs(difference)
max_value = max(number_x, number_y)
min_value = min(number_x, number_y)

print("Sum: %d  Difference: %d  Product: %d  Average_value: %.2f  Distance: %d  Max_value: %d  Min_value: %d " 
      %(sum, difference, product, average_value, distance, max_value, min_value))