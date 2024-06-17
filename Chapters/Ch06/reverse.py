def main():
    numbers = read_floats(5)
    multiply(numbers, 10)
    print_reversed(numbers)

def read_floats(number_of_inputs): 
    print("Enter", number_of_inputs,"numbers: ")
    inputs = []
    for i in range(number_of_inputs):
        value = float(input(""))
        inputs.append(value)
    return inputs # le funzioni possono ritornare una lista

def multiply(values, factor): # una lista può essere passata come argomento
    for i in range(len(values)):
        values[i] *= factor

def print_reversed(values):
    i = len(values) - 1 # i prende la posizione dell'ultimo elemento nella lista
    while i >= 0 :
        print(values[i], end=" ") # end="" è il contrario di "\n", quindi l'output avviene sulla stessa riga
        i -= 1
    print()

main()
