import json
import os
from models.expense import Expense


class ExpenseManager:
    def __init__(self, expense_file="tools/expenses.json"):
        self.expense_file = expense_file

        if not os.path.exists(self.expense_file):
            with open(self.expense_file, "w") as file:
                json.dump([], file)

    def add_expenses(self, name, amount, category, date):
        expense = Expense(name, amount, category, date).dict()
        with open(self.expense_file, "r") as file:
            expenses = json.load(file)

            expenses.append(expense)
            with open(self.expense_file, "w") as file:
                json.dump(expenses, file)

    def retrieve_expenses(self):
        with open(self.expense_file, "r") as file:
            return json.load(file)
