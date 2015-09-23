def calculateFinalSum(moInRate, suggestedLowestPayment, balance):
    updatedBalanceEachMonth = balance
    for i in range(1, 13):
        montlyUnpaidBalance = updatedBalanceEachMonth - suggestedLowestPayment
        updatedBalanceEachMonth = montlyUnpaidBalance + (moInRate * montlyUnpaidBalance)
    return updatedBalanceEachMonth


# input
balance = 3329
annualInterestRate = 0.2

# firstCalculations
monthlyInterestRate = annualInterestRate / 12.0
suggestedLowestPayment = balance / 12 + (10 - (balance / 12) % 10)
while calculateFinalSum(monthlyInterestRate, suggestedLowestPayment, balance) > 0:
    suggestedLowestPayment += 10

print  "Lowest Payment: ", suggestedLowestPayment