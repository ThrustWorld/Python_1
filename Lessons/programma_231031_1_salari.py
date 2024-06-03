total = 0.0 # somma dei valori immessi
n = int(input("Quanti salari vuoi inserire? "))
for j in range(n):
    salary = float(input("Immetti salario: "))
    total += salary
if n > 0:
    average = total / n
    print("La media dei salari è", average)
else:
    print("Nessun dato immesso")
