import math

# ask user to enter loan principal
principal = float(input("Enter the loan principal"))

# ask user what they want to calculate
calculation = input('Enter "m" to calculate number of monthly payments or "p" to calculate monthly payment amount: ')

# calculate the number of monthly payments
if calculation == 'm':
    # ask user to enter the monthly payment amount
    monthly_payment = float(input("What's your monthly payment"))

    # calculate the number of months
    months = principal/monthly_payment

    # round up the number of months
    months = math.ceil(months)
    # calculate the last payment
    last_payment = principal - (months - 1) * monthly_payment
    print(months)
    # print the results
    print(f"It will take you {months} months to repay this loan")
    if last_payment == monthly_payment:
        print(f"The monthly payment will be: {monthly_payment}$")
    else:
        print(f"The monthly payment will be: {monthly_payment}$ and the last payment will be {last_payment}$")

# calculate the monthly_payment amount
if calculation == 'p':
    # ask user to enter the number of months
    months = int(input("How many months will you be paying?"))

    # calculate the monthly_payment
    monthly_payment = principal / months

    # round up the monthly payment
    monthly_payment = math.ceil(monthly_payment)

    # calculate the last payment
    last_payment = principal - (months - 1) * monthly_payment

    # print the results
    if last_payment == monthly_payment:
        print(f"in {months} months it you will have to pay {monthly_payment}$ each month")
    else:
        print(f"in {months} months it you will have to pay {monthly_payment}$ each month and {last_payment}$ the last month")
