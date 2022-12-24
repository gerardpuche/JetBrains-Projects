import math # import math module for log and ceil functions

# ask user what they want to calculate
calculation = input('Enter "n" to calculate number of monthly payments, "a" to calculate annuity monthly payment amount or "p" to calculate the loan principal: ')

#make cases for each calculation

#calculate monthly payments
if calculation == "n":
    #ask loan principal
    p = int(input("Enter the loan principal: "))
    #ask montly payment
    a = float(input("Enter your monthly payment"))
    #ask interest rate
    interest_in_percentage = float(input("Enter your interest rate:"))
    #convert interest rate to decimal
    i = float((interest_in_percentage/12)/100) 
    #calculate the number of monthly payments
    n = math.log(a/(a - i * p), 1+i)
    #round up to the nearest whole number
    n = math.ceil(n)
    #calculate number of years
    years = int(n//12)
    #calculate number of months
    rest_of_months = math.ceil(n % 12)
    #print result
    if n < 12:
        print("It will take you", round(n), "months to repay this loan")
    elif rest_of_months == 0:
        print(f"It will take you {years} years")
    else:
        print(f"It will take you {years} years and {rest_of_months} months to repay this loan")

#calculate monthly payment amount
if calculation == "a":
    #ask loan principal
    p = int(input("Enter the loan principal: "))
    #ask number of monthly payments
    n = int(input("Enter the number of monthly payments"))
    #ask interest rate
    interest_in_percentage = float(input("Enter your interest rate:"))
    #convert interest rate to decimal
    i = (interest_in_percentage/12)/100
    #calculate the monthly payment amount
    a = p * ((i*(1+i)**n)/((1+i)**n - 1))
    #round up to the nearest whole number
    a = math.ceil(a)
    #print result
    print(f"Your monthly payment will be {a}")

#calculate loan principal
if calculation == "p":
    #ask montly payment
    a = float(input("Enter your monthly payment"))
    #ask number of monthly payments
    n = int(input("Enter the number of monthly payments"))
    #ask interest rate
    interest_in_percentage = float(input("Enter your interest rate:"))
    #convert interest rate to decimal
    i = (interest_in_percentage/12)/100
    #calculate the loan principal
    p = a/((i*(1+i)**n)/((1+i)**n - 1))
    #round up to the nearest whole number
    p = math.ceil(p)
    #print result
    print(f"The loan principal will be {p}")

