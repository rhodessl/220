"""
Name: Shelby Rhodes
interest.py

Problem: This program computes the monthly interest charge on a credit card account

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    annual_interest_rate = eval(input("What is the annual interest rate?"))
    days_billing_cycle = eval(input("What is the number of days in the billing cycle?"))
    net_balance = eval(input("What is the previous net balance?"))
    total_x = net_balance * days_billing_cycle
    total_x = round(total_x, 2)
    payment = eval(input("What is the payment amount?"))
    day_of_billing_cycle = eval(input("What is the day of the billing cycle the payment was made?"))
    days_before_end_cycle = days_billing_cycle - day_of_billing_cycle
    total_y = payment * days_before_end_cycle
    total_y = round(total_y, 2)
    total_a = total_x - total_y
    total_a = round(total_a, 2)
    average_daily_balance = total_a / days_billing_cycle
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_interest_charge = average_daily_balance * monthly_interest_rate
    print(round(monthly_interest_charge, 2))

if __name__ == "__main__":
    main()
