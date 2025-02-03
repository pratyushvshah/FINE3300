# Function to calculate the monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly and rapid weekly payments
def mortgage_payments(principal, rate, amortization):
    monthly_rate = ((1 + rate/2)**(2/12) - 1)
    semi_monthly_rate = ((1 + rate/2)**(2/24) - 1)
    bi_weekly_rate = ((1 + rate/2)**(2/26) - 1)
    weekly_rate = ((1 + rate/2)**(2/52) - 1) 
    monthly_payment = principal * (((monthly_rate) * ((1 + monthly_rate)**(amortization*12)))/(((1 + monthly_rate)**(amortization*12)) - 1))
    semi_monthly_payment = principal * (((semi_monthly_rate) * ((1 + semi_monthly_rate)**(amortization*24)))/(((1 + semi_monthly_rate)**(amortization*24)) - 1))
    bi_weekly_payment = principal * (((bi_weekly_rate) * ((1 + bi_weekly_rate)**(amortization*26)))/(((1 + bi_weekly_rate)**(amortization*26)) - 1))
    weekly_payment = principal * (((weekly_rate) * ((1 + weekly_rate)**(amortization*52)))/(((1 + weekly_rate)**(amortization*52)) - 1))
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
    return (round(monthly_payment,2), round(semi_monthly_payment,2), round(bi_weekly_payment,2), round(weekly_payment,2), round(rapid_bi_weekly_payment,2), round(rapid_weekly_payment,2))

if __name__ == "__main__":

    # Take user input for principal, rate, and amortization
    input_principal = float(input("Enter the principal amount: "))
    input_interest = float(input("Enter the interest rate: "))/100
    input_amortization = int(input("Enter the amortization period: "))

    # Call the payments function
    monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment = mortgage_payments(input_principal, input_interest, input_amortization)

    # Print the calculated payments
    print("Monthly Payment: ", monthly_payment)
    print("Semi-Monthly Payment: ", semi_monthly_payment)
    print("Bi-Weekly Payment: ", bi_weekly_payment)
    print("Weekly Payment: ", weekly_payment)
    print("Rapid Bi-Weekly Payment: ", rapid_bi_weekly_payment)
    print("Rapid Weekly Payment: ", rapid_weekly_payment)
