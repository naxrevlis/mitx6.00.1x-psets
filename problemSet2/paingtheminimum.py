# functions to calc
def minMonthlyPayment(monthlyPaymentRate, remainingBalance):
    return monthlyPaymentRate * remainingBalance

# Input variables
balance = 4213
annualInterestRate = 0.2
montlyInterestRate = annualInterestRate / 12
monthlyPaymentRate = 0.04

# Define variables
minimumMonthlyPayment = 0
remainingBalance = balance
totalPaid = 0
montlyUnpaidBalance = balance

for i in range(1, 13):
    minimumMonthlyPayment = minMonthlyPayment(monthlyPaymentRate, remainingBalance)
    montlyUnpaidBalance = remainingBalance - minimumMonthlyPayment
    remainingBalance = montlyUnpaidBalance + (montlyInterestRate * montlyUnpaidBalance)
    totalPaid += minimumMonthlyPayment
    print "Month", i
    print "Minimum monthly payment: {:.2f}".format(minimumMonthlyPayment)
    print "Remaining balace: {:.2f}".format(remainingBalance)

# total output
print "TotalPaid: {:.2f}".format(totalPaid)
print "Remaining balance: {:.2f}".format(remainingBalance)
