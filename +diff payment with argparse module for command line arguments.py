import math # import math module for log and ceil functions
import argparse

parser = argparse.ArgumentParser(description="This program prints calculates the variables of a loan given the other data.")

parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()


if args.type == "annuity":

    #make cases for each calculation

    #calculate monthly payments
    if args.principal and args.payment and args.interest:
        #ask loan principal
        p = int(args.principal)
        #ask montly payment
        a = int(args.payment)
        #ask interest rate
        interest_in_percentage = float(args.interest)
        #convert interest rate to decimal
        i = float((interest_in_percentage/12)/100) 
        #calculate the number of monthly payments
        n = math.log(a / (a - i * p), 1 + i)
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

        overpayment = a * n - p
        print(overpayment)

    else:
        print("Incorrect parameters.")


    #calculate monthly payment amount
    if args.principal and args.periods and args.interest:
        #ask loan principal
        p = int(args.principal)
        #ask number of monthly payments
        n = int(args.periods)
        #ask interest rate
        interest_in_percentage = float(args.interest)
        #convert interest rate to decimal
        i = float((interest_in_percentage/12)/100)
        #calculate the monthly payment amount
        a = math.ceil(p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        #round up to the nearest whole number
        a = math.ceil(a)
        #print result
        print(f"Your monthly payment will be {a}")

        overpayment = a * n - p
        print(overpayment)

    else:
        print("Incorrect parameters.")

    #calculate loan principal
    if args.payment and args.periods and args.interest:
        #ask montly payment
        a = int(args.payment)
        #ask number of monthly payments
        n = int(args.periods)
        #ask interest rate
        interest_in_percentage = float(args.interest)
        #convert interest rate to decimal
        i = (interest_in_percentage/12)/100
        #calculate the loan principal
        p = math.floor(a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)))
        #print result
        print(f"The loan principal will be {p}")

        overpayment = a * n - p
        print(overpayment)
        
    else:
        print("Incorrect parameters.")

if args.type == "diff":
    if args.principal and args.periods and args.interest:
        #ask loan principal
        p = int(args.principal)
        #ask number of monthly payments
        n = int(args.periods)
        #ask interest rate
        interest_in_percentage = float(args.interest)
        #convert interest rate to decimal
        interest = (interest_in_percentage/12)/100
        
        total = 0
        for m in range (1, n + 1):
            d = math.ceil(p/n + interest* (p-((p*(m-1))/n)))
            total += d
            print(f"Month {m}: {d}")
                
            
        print(f"Your overpayment is: {total - p}")

    else:
        print("Incorrect parameters.")
