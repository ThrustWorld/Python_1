def main():
    print("Enter a time: hours and minutes.")
    hours = read_int_between(0,23) # una funzione può essere riutilizzata per ritornare un valore a più di una variabile
    minutes = read_int_between(0,59)
    print("You entered %d hours and %d minutes" % (hours, minutes))

def read_int_between(low,high):
    value = int(input("Enter a value between " + str(low) + " and " + str(high) + ": "))
    while value < low or value > high:
        print("Error: value out of range")
        value = int(input("Enter a value between " + str(low) + "and " + str(high) + ": "))
    return value

main()