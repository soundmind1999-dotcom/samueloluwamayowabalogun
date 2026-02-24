loan_amount = float(input("Enter loan amount: "))
number_of_years = int(input("Enter number of years: "))

print("\nInterest Rate\tMonthly Payment\tTotal Payment")

for number in range(20, 41):   
    rate = number / 4
    monthly_interest_rate = rate / 100 / 12
    number_of_months = number_of_years * 12

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - 1 / (1 + monthly_interest_rate) ** number_of_months)
    total_payment = monthly_payment * number_of_months

    print(f"{rate:.3f}%\t\t{monthly_payment:.2f}\t\t{total_payment:.2f}")
