def calculateFinalSum(moInRate, suggestedLowestPayment, balance):
    updatedBalanceEachMonth = balance
    for i in range(1, 13):
        montlyUnpaidBalance = updatedBalanceEachMonth - suggestedLowestPayment
        updatedBalanceEachMonth = montlyUnpaidBalance + (moInRate * montlyUnpaidBalance)
    return updatedBalanceEachMonth

# input
balance = 320000
annualInterestRate = 0.2

# firstCalculations
monthlyInterestRate = annualInterestRate / 12.0
suggestedLowestPayment = balance / 12.0
low = suggestedLowestPayment
high = (balance * (1 + monthlyInterestRate)**12)/12.0
test = calculateFinalSum(monthlyInterestRate, low, balance)
accuracy = 0.01


while abs(test) > 0.01:
    c = (high+low)/2
    test = calculateFinalSum(monthlyInterestRate, c, balance)
    if test < 0:
       high = c
    else:
       low = c

print  "Lowest Payment: {:.2f}".format(c)