monthly_income = 5000
monthly_expenses = 4000
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings* 12*0.05)
print("Enter your monthly income: "+str(monthly_income))
print("Enter your total monthly expenses: "+ str(monthly_expenses))
print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $"+ str(projected_savings))
