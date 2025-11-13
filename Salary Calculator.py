# Simple Salary Calculator

# Given values
hours_worked = 30
hourly_rate = 9
tax_rate = 0.1  # 10% tax

# Calculate gross pay, tax, and net pay
gross_pay = hours_worked * hourly_rate
tax = gross_pay * tax_rate
net_pay = gross_pay - tax

# Display results
print("--- Weekly Pay Summary ---")
print("Hours worked:", hours_worked)
print("Hourly rate: $", hourly_rate)
print("Gross pay: $", gross_pay)
print("Tax (10%): $", tax)
print("Net pay: $", net_pay)
