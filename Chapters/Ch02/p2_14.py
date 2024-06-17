number = input("Please enter an integer between 1000 and 999999:")

number = number[0:-3] + "," + number[-3:] # Slincing -> presa di sottostringhe dalla posizione i alla posizione j non inclusa [i:j]

print(number)