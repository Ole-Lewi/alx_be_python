# Prompt the user to enter their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12  # Total savings over 12 months
annual_interest = annual_savings * 0.05  # 5% annual interest
projected_savings = annual_savings + annual_interest

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
