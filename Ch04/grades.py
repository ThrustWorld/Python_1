num_passing = 0
num_failing = 0

total = 0.0
count = 0

min_grade = 100
max_grade = 0

grade = float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0 : # Ciclo finchè condizione soddisfatta
    if grade >= 60.0 :
        num_passing += 1
    else :
        num_failing += 1

    if grade < min_grade : # Ricerca del minimo e del massimo
        min_grade = grade
    if grade > max_grade :
        max_grade = grade
    
    total += grade
    count += 1

    grade = float(input("Enter a grade or -1 to finish: "))

if count > 0 :
    average = total / count
    print("Average: ", average)
    print("Number of failing grades: ", num_failing)
    print("Number of passing grades: ", num_passing)
    print("Maximum grade: ", max_grade)
    print("Minimum grade: ", min_grade)