import math
print('What do you want to calculate? \n '
      'type "n" for number of monthly payments, \n '
      'type "a" for annuity monthly payment amount, \n '
      'type "p" for loan principal:')

choose_type = input()

def number_of_monthly():
    loan_principal = int(input('Enter the loan principal: '))
    monthly_payment = int(input('Enter the monthly payment: '))
    loan_interest = float(input('Enter the loan interest: '))

    interest_rate = (loan_interest / 100) / 12
    number_of_months = math.ceil(math.log(monthly_payment / (monthly_payment - interest_rate * loan_principal), 1 + interest_rate))
    year, month = number_of_months // 12, number_of_months % 12

    if year == 0:
        print(f'It will take {month} months to repay this loan!')
    elif month == 0:
        print(f'It will take {year} years to repay this loan!')
    else:
        print(f'It will take {year} years and {month} months to repay this loan!')

def summ_of_month():
    loan_principal = int(input('Enter_the_loan_principal: '))
    number_of_period = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest:'))

    interest_rate = (loan_interest / 100) / 12
    summ_of_paid = loan_principal * ((interest_rate * math.pow(1 + interest_rate, number_of_period)) / (math.pow(1 + interest_rate, number_of_period) - 1))

    print(f'Your monthly payment = {math.ceil(summ_of_paid)}')

def loan_principal():
    annuity_payment = float(input('Enter the annuity payment:'))
    number_of_period = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest:'))

    interest_rate = (loan_interest / 100) / 12
    loan_principal = annuity_payment /((interest_rate * math.pow(1 + interest_rate, number_of_period)) / (math.pow(1 + interest_rate, number_of_period) - 1))
    print(f'Your loan principal = {round(loan_principal)}')
if choose_type == 'n':
    number_of_monthly()
elif choose_type == 'a':
    summ_of_month()
elif choose_type == 'p':
    loan_principal()
