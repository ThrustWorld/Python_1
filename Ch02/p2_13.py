number = input("Please enter an integer between 10,000 and 99,999: ")

# Take the single chars to remove comma
first_char = number[0]
second_char = number[1]
fourth_char = number[3]
fifth_char = number[4]
sixth_char = number[5]

# Compose the chars to a single number
number = first_char + second_char + fourth_char + fifth_char + sixth_char

number_to_int = int(number)

print(number)