from decimal import *
import calculation

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
        print("You have not recorded an expense yet!")
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
        print("3. Calculate Total Expenses")
        print("4. Calcualte Average Monthly Expense")
        print("5. Exit")

        userChoice = input("Enter the value of the item you wish to do: ")

        if userChoice == "1":
            date = input("Enter the date of the expense (i.e mm-dd-yyyy): ")
            amount = float(input("Enter the expense amount: $"))
            description = input("Enter the description of the expense: ")
            add_expense(date, amount, description)
        elif userChoice == "2":
            view_expenses()
        elif userChoice == "3":
            total = calculation.calculate_total_expenses(expenses)
            print(f"\nTotal Expenses: ${total:.2f}")
        elif userChoice == "4":
            monthly_average = calculation.calculate_average_monthly_expense(expenses)
            print(f"\nAverage Monthly Expense: ${monthly_average:.2f}")
        elif userChoice == "5":
            break
        else:
            print("Invalid choice! Please try again.")