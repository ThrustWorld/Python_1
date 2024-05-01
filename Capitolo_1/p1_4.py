start_balance = 1000
interest = 0.05

first_year_balance = (start_balance * interest) + start_balance
second_year_balance = (first_year_balance * interest) + first_year_balance
third_year_balance = (second_year_balance * interest) + second_year_balance

print("First year balance: ",first_year_balance)
print("Second year balance: ",second_year_balance)
print("Third year balance: ",third_year_balance)
