# Financial Advising app, aim is to give feedback to users about their financial situation quickly
# Purpose: Help users stay more aware of their financial situation, so that they don't make bad
# decisions, such as overcharging credit cards

import datetime
from datetime import date

def income(bal, num):
    return bal + num
def expenditure(bal, num):
    return bal-num
def status(bal, target):
    tem = target/4
    if bal <= 0:
        return "In debt"
    elif bal > target:
        return "Excellent"
    elif bal <= tem:
        return "Low"
    elif bal <= 2*tem:
        return "Okay"
    elif bal <= 3*tem:
        return "Good"
    else:
        return "Great"
def balance_advice(bal, target):
    temp = target/4
    if bal > target:
        return "You are saving well! Consider investing some money."
    elif bal <= temp:
        return "Your personal balance is critically low, cut any unnecessary spending"
    elif bal <= 2*temp:
        return "Your balance is somewhat low, consider saving more money to reach your ideal balance"
    elif bal <= 3*temp:
        return "Continue saving! You can reach your target balance"
    else: # balance is 3/4 - 4/4 of target
        return "You balance is in a good position"
def monthly_spending_advice(monthexp, budg):
    temp = budg / 4
    if monthexp > budg:
        return "Your monthly expenses has exceeded your budget of " + str(budg) + ", cut down any unnecessary spending"
    elif monthexp < temp:
        return "Your expenses for this month have been low, you are doing well staying within your budget!"
    elif monthexp < 2*temp:
        return "You are still well within your budget."
    elif monthexp < 3*temp:
        return "You have already spent half your budget for this month. Plan ahead"
    else: # Have spent btwn 3/4 and all of their monthly budget
        return "You have nearly spent all of your monthly budget. Spend carefully!"
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
def display_info(bal, month, month_expenditure, budget, targ):
    print("---------------------------------------------------------")
    print("Current Balance:", bal)
    print("Status:", status(bal, targ))
    print("Advice:", balance_advice(bal, targ))
    print()
    print("Month: ", give_month(month))
    print("Monthly Expenses:", month_expenditure)
    print("Advice: ", monthly_spending_advice(month_expenditure, budget))
    print("---------------------------------------------------------")


def main():
    print("Welcome to Your Income Tracker\n")
    # Take basic information, like current balance, monthly budget, and ideal balance
    print("Introductory Information")
    balance = float(input("What is your current balance? "))
    target = float(input("What is your ideal balance? "))
    bud = float(input("How much do you want to spend each month? Enter your budget: "))
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
            if add >= 0:
                balance = income(balance, add)
            else:
                print("Error: income cannot be negative")
            display_info(balance, current_month, monthexp, bud, target)
        elif choice == '-1':
            sub = float(input("How much money did you spend: "))
            if sub >= 0:
                monthexp += sub
                balance = expenditure(balance, sub)
            else:
                print("Error: Expenditure cannot be a negative number")
            display_info(balance, current_month, monthexp, bud, target)
        elif choice == '0':
            print("Exiting Tracker...")
            break
        else:
            print("Please enter one of the options:\n1 to enter income\n-1 to enter an expense\n0 to exit")
        choice = input("What would you like to do? ")

main()