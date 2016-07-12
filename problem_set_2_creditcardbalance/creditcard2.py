balance =  3926
annualInterestRate = 0.2

currentBalance = balance
minimumMonthlyPayment = 0
while currentBalance >= 0:
    totalPaid = 0
    currentBalance = balance
    minimumMonthlyPayment += 0.001
    for i in range(12):
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = currentBalance - minimumMonthlyPayment
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        currentBalance = updatedBalanceEachMonth
        totalPaid += minimumMonthlyPayment

print 'Lowest payment: ' + str(minimumMonthlyPayment)

