# Function to calculate the monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly and rapid weekly payments
def mortgage_payments(principal, interest, ammortization):
    monthly_rate = ((1 + interest/2)**(2/12) - 1)
    semi_monthly_rate = ((1 + interest/2)**(2/24) - 1)
    bi_weekly_rate = ((1 + interest/2)**(2/26) - 1)
    weekly_rate = ((1 + interest/2)**(2/52) - 1) 
    monthly_payment = principal * (((monthly_rate) * ((1 + monthly_rate)**(ammortization*12)))/(((1 + monthly_rate)**(ammortization*12)) - 1))
    semi_monthly_payment = principal * (((semi_monthly_rate) * ((1 + semi_monthly_rate)**(ammortization*24)))/(((1 + semi_monthly_rate)**(ammortization*24)) - 1))
    bi_weekly_payment = principal * (((bi_weekly_rate) * ((1 + bi_weekly_rate)**(ammortization*26)))/(((1 + bi_weekly_rate)**(ammortization*26)) - 1))
    weekly_payment = principal * (((weekly_rate) * ((1 + weekly_rate)**(ammortization*52)))/(((1 + weekly_rate)**(ammortization*52)) - 1))
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
    return (round(monthly_payment,2), round(semi_monthly_payment,2), round(bi_weekly_payment,2), round(weekly_payment,2), round(rapid_bi_weekly_payment,2), round(rapid_weekly_payment,2))

# Function to take user input and call the mortgage class to calculate the payments
def main():   
    input_principal = float(input("Enter the principal amount: "))
    input_interest = float(input("Enter the interest rate: "))/100
    input_ammortization = int(input("Enter the ammortization period: "))

    # Call the payments function from the mortgage class
    monthly_payment, semi_monthly_payment, bi_weekly_payment, weekly_payment, rapid_bi_weekly_payment, rapid_weekly_payment = mortgage_payments(input_principal, input_interest, input_ammortization)

    # Print the calculated payments
    print("Monthly Payment: ", monthly_payment)
    print("Semi-Monthly Payment: ", semi_monthly_payment)
    print("Bi-Weekly Payment: ", bi_weekly_payment)
    print("Weekly Payment: ", weekly_payment)
    print("Rapid Bi-Weekly Payment: ", rapid_bi_weekly_payment)
    print("Rapid Weekly Payment: ", rapid_weekly_payment)

# Call the main function
if __name__ == "__main__":
    main()



