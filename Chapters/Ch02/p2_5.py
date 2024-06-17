number_x = int(input("Digita un primo numero: "))
number_y = int(input("Digita un secondo numero: "))

sum = number_x + number_y
difference = number_x - number_y
product = number_x * number_y
average_value = sum / 2
distance = abs(difference)
max_value = max(number_x, number_y)
min_value = min(number_x, number_y)

print("%11s %10d" %("Sum:", sum))
print("%11s %10d" %("Difference:", difference))
print("%11s %10d" %("Product:", product))
print("%11s %10.2f" %("Average:", average_value))
print("%11s %10d" %("Distance:", distance))
print("%11s %10d" %("Max:", max_value))
print("%11s %10d" %("Min:", min_value))