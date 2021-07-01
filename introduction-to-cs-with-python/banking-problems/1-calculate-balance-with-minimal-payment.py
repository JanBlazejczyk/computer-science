'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. 
At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy - so print: Remaining balance: 813.41
instead of Remaining balance: 813.4141998135 
'''

month = 0

for i in range(12):
    # minimum payment in the given month is deducted from the balance
    balance = balance - (monthlyPaymentRate * balance)
    # month passess
    month += 1
    # new balance is calculated
    balance = balance + ((annualInterestRate / 12) * balance)

print('Remaining balance:', ("%.2f" % balance))
