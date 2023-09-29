from collections import defaultdict
from datetime import datetime

def calculate_total_expenses(expenses):
    total_expenses = sum(expense['amount'] for expense in expenses)
    return total_expenses

def calculate_average_monthly_expense(expenses):
    monthly_expense = defaultdict(float)
    for expense in expenses:
        date = datetime.strptime(expense["date"], "%Y-%m-%d")
        month_date = date.strftime("%Y-%m")
        monthly_expense[month_date] += expense["amount"]

    total_months = len(monthly_expense)
    total_expense = sum(monthly_expense.values())
    if total_months == 0:
        return 0
    else:
        return total_expense / total_months