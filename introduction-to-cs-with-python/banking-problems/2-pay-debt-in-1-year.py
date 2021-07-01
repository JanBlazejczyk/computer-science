'''
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

 The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, 
 for example: Lowest Payment: 180 

'''

final_balance = -1

# initial value of payment
payment = 0
run = True

while run:

    payment += 10
    final_balance = balance

    # balance after 12 payments with the fixed amount
    for i in range(12):
        if i == 0:
            final_balance = balance - payment
            final_balance = final_balance + \
                ((annualInterestRate / 12) * final_balance)
        else:
            final_balance = final_balance - payment
            final_balance = final_balance + \
                ((annualInterestRate / 12) * final_balance)

    if final_balance <= 0:
        run = False

print('Lowest Payment:', payment)
