from decimal import *

def add_expense(date, amount, description):
    expense = {
        "date": date,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Successfully added to tracker.")

def view_expenses():
    if not expenses:
        print("You have not recoreded an expense yet!")
    else:
        print("List of expenses")
        print("----------------")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. Date: {expense['date']}, Amount: ${expense['amount']}, Description: {expense['description']}")

if __name__ == "__main__":

    expenses = []

    while True:
        print("\n Expense Tracker ")
        print("-----------------\n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        userChoice = input("Enter the value of the item you wish to do: ")

        if userChoice == "1":
            date = input("Enter the date of the expense (i.e mm-dd-yyyy): ")
            amount = Decimal(input("Enter the expense amount: $"))
            description = input("Enter the description of the expense: ")
            add_expense(date, amount, description)
        elif userChoice == "2":
            view_expenses()
        elif userChoice == "3":
            break
        else:
            print("Invalid choice! Please try again.")