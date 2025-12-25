
principal = float(input("Enter loan principal: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan duration (years): "))

monthly_rate = annual_rate / (100 * 12)
months = years * 12

monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print(f"Monthly Mortgage Payment: {monthly_payment:.2f}")

