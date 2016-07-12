balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid =0
for i in range(12):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    balance =  updatedBalanceEachMonth
    totalPaid += minimumMonthlyPayment
    print 'Month: ' + str(i+1)
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2))
    print 'Remaining balance: ' + str(round(updatedBalanceEachMonth,2))

print 'Total paid: '+str(round(totalPaid,2))
print 'Remaining balance: ' + str(round(updatedBalanceEachMonth,2))