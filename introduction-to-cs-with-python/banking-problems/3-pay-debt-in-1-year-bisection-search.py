'''
Calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code, use bisection search

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year
'''

final_balance = -1

# initial values of payment
lower_payment = balance / 12
monthlyIntrestRate = annualInterestRate / 12
higher_payment = (balance * (1 + monthlyIntrestRate) ** 12) / 12.0

counter = 0

while True:
    counter += 1
    # each time payment = (lower_payment + higher_payment) / 2
    payment = (lower_payment + higher_payment) / 2

    # each time we try to pay off the same balance
    final_balance = balance

    # calculate the balance after 12 fixed payments
    for i in range(12):
        if i == 0:
            final_balance = balance - payment
            final_balance = final_balance + \
                ((annualInterestRate / 12) * final_balance)
        else:
            final_balance = final_balance - payment
            final_balance = final_balance + \
                ((annualInterestRate / 12) * final_balance)

    if final_balance < -0.015:
        higher_payment = payment

        continue
    if final_balance > 0.015:
        lower_payment = payment
        continue
    else:
        print("Lowest payment is:", ("%.2f" % payment))
        break
