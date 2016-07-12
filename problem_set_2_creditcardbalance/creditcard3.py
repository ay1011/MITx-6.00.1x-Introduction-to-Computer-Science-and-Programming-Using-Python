def remaining_debt(annual_ir, new_balance, min_monthly_payment):
    monthly_interest_rate = annual_ir / 12.0
    for i in range(12):
        monthly_unpaid_balance = float(new_balance - min_monthly_payment)
        updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        new_balance = updated_balance_each_month
    return updated_balance_each_month



balance = 3926
annualInterestRate = 0.2

currentBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLower = balance / 12
monthlyPaymentUpper = (balance * (1 + monthlyInterestRate)**12) / 12.0

while abs(currentBalance) > 0.001:
    currentBalance = balance
    minimumMonthlyPayment = (monthlyPaymentUpper + monthlyPaymentLower) / 2
    currentBalance = remaining_debt(annualInterestRate, balance, minimumMonthlyPayment)
    if currentBalance > 0:
        monthlyPaymentLower = minimumMonthlyPayment
    elif currentBalance < 0:
        monthlyPaymentUpper = minimumMonthlyPayment

print 'Lowest payment: ' + str(round(minimumMonthlyPayment, 2))

