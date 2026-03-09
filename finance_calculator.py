# Finance Calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
savings = monthly_income - monthly_expenses
I = 0.05
annual_savings = savings * 12 + (savings * I * 12)
print(f'Your monthly savings are: ${savings}')
print(f'Projected savings after one year, with interest is: ${annual_savings}')