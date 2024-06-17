def main():
    richter = float(input("Enter a magnitude on the Richter scale: "))

    description = get_description(richter)
    print(description)

def get_description(richter):
    if richter >= 8.0:
        result = "Most structure fail"
    elif richter >= 7.0:
        result = "Many buildings destroyed"
    elif richter >= 4.5:
        result = " Damage to poorly constructed buildings"
    else :
        result = "No destruction of buildings"
    return result # ritorna il valore e lo assegna alla variabile che ha invocato la funzione

main()