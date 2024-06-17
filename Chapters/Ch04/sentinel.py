total = 0.0
count = 0

salary = 0.0

while salary >= 0.0 :
    salary = float(input("Enter a salary or -1 to finish: ")) # -1 è una sentinella, ovvero un valore non presente tra i dati di ingresso che ci permette di uscire dal ciclo
    if salary >= 0.0 :
        total = total + salary
        count = count + 1

if count > 0 :
    average = total / count
    print("Average salary: ", average)
else: 
    print("No data was entered")