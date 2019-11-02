import datetime
from datetime import date

def income(bal, num):
    return bal + num
def expenditure(bal, num):
    return bal-num
def status(bal):
    if bal <= 0:
        return "In debt; spend wisely"
    elif bal <= 1000:
        return "Balance critically low"
    elif bal <= 5000:
        return "Okay"
    elif bal > 80000:
        return "Excellent"
    else:
        return "Good"
def advice(bal):
    if bal <= 1000:
        return "You"
    elif bal <= 1000:
        return "Your personal balance is critically low, cut unnecessary spending"
    elif bal <= 5000:
        return "Your balance is somewhat low, unnecessary spending is not advised right now"
    elif bal > 80000:
        return "You are in good standing, consider investing some money"
    else:
        return "You are in good standing"
def give_month(num):
    if num == 1:
        return "January"
    elif num == 2:
        return "February"
    elif num == 3:
        return "March"
    elif num == 4:
        return "April"
    elif num == 5:
        return "May"
    elif num == 6:
        return "June"
    elif num == 7:
        return "July"
    elif num == 8:
        return "August"
    elif num == 9:
        return "September"
    elif num == 10:
        return "October"
    elif num == 11:
        return "November"
    elif num == 12:
        return "December"

def display_info(bal, month, month_expenditure):
    print("---------------------------------------------------------")
    print("Current Balance:", bal)
    print("Status:", status(bal))
    print("Advice:", advice(bal))
    print()
    print("Month: ", give_month(month))
    print("Monthly Expenses:", month_expenditure)
    print("---------------------------------------------------------")

def main():
    print("Welcome to Your Income Tracker")
    print("Introductory Information")
    # Take basic information, like current balance and annual income
    balance = float(input("What is your current balance? "))
    print()
    # Monthly expenditures
    # Get current month
    now = date.today()
    current_month = now.month # Gives current month as an integer btwn 1 and 12
    monthexp = 0

    # Menu options - income, expenditures, view balance
    print("Enter income: Press 1")
    print("Enter an expense, Press -1")
    print("To exit program, Press 0")
    choice = input()
    while choice != 0:
        if choice == '1':
            add = float(input("Enter how much money you received: "))
            balance = income(balance, add)
            display_info(balance, current_month, monthexp)
        if choice == '-1':
            sub = float(input("How much money did you spend: "))
            monthexp += sub
            balance = expenditure(balance, sub)
            display_info(balance, current_month, monthexp)

        if choice == '0':
            print("Exiting Tracker...")
            break

        choice = input()

main()