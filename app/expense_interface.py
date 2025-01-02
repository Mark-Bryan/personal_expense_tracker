from tkinter import *
import tkinter.messagebox as box
import os
from datetime import datetime
from models.expense import Expense
from models.manager import ExpenseManager


class ExpenseTracker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Personal Expense Tracker")

        self.expense_manager = ExpenseManager("data/expenses.json")

        self.current_user = None
        self.user_file = "users.json"
        self.login_frame = None
        self.register_frame = None
        self.main_frame = None

        self.login_screen()

    def initialise_user_screen(self):
        """Initialises the user file if it doesn't exist"""
        if not os.path.exists(self.user_file):
            print(
                f"The user file '{self.user_file} 'does not exist. Please create it manually"
            )

    def login_screen(self):
        """Shows the login screen"""
        if self.login_frame:
            self.login_frame.destroy()
        self.login_frame = Frame(self.window)
        self.login_frame.pack(pady=15)

        login_label = Label(
            self.login_frame, text="Login", font=("Times New Roman", 18)
        )
        login_label.pack()

        name_label = Label(self.login_frame, text="Username: ")
        name_label.pack()

        username_entry = Entry(self.login_frame)
        username_entry.pack()

        pwd_label = Label(self.login_frame, text="Password: ")
        pwd_entry = Entry(self.login_frame, show="*")
        pwd_entry.pack()
        pwd_label.pack()

        def login():
            username = username_entry.get()
            password = pwd_entry.get()

            login_btn = Button(self.login_frame, text="LogIn", command=login)
            login_btn.pack(pady=5)

            reg_btn = Button(self.login_frame, text="Register", command=register_screen)
            reg_btn.pack()

        def register_screen():
            """Shows the register screen"""
            if self.login_frame:
                self.login_frame.destroy()
            self.register_frame = Frame(self.window)
            self.register_frame.pack(pady=20)

            reg_label = Label(
                self.register_frame, text="Register", font=("Times New Roman", 18)
            )
            reg_label.pack()

            fullname_label = Label(self.register_frame, text="Full Name:")
            full_name_entry = Entry(self.register_frame)
            fullname_label.pack()
            full_name_entry.pack()

            pd_label = Label(self.register_frame, text="Password")
            pd_label.pack()

            pd_entry = Entry(self.register_frame, show="*")
            pd_entry.pack()

            def register():
                full_name = full_name_entry.get()
                username = username_entry.get()
                password = pwd_entry.get()

            reg_btn = Button(self.register_frame, text="Register", command=register)
            reg_btn.pack()
            lgnI_btn = Button(
                self.register_frame, text="Back To Login", command=main_screen
            )
            lgnI_btn.pack()

        def main_screen():
            """Shows the main screen after login"""
            if self.login_frame:
                self.login_frame.destroy()
            if self.register_frame:
                self.register_frame.destroy()

            self.main_frame = Frame(self.window)
            self.main_frame.pack(pady=20)

            wlcLabel = Label(
                self.main_frame,
                text=f"Welcome, {self.current_user}",
                font=("Times New Roman", 18),
            )
            wlcLabel.pack()

            check_button = Button(self.main_frame, text="Check Expenses")
            check_button.pack(padx=5)

    def add_expenses(self):
        if self.main_frame:
            self.main_frame.destroy()

            self.add_expense_frame = Frame(self.window)
            self.add_expense_frame.pack(pady=20)

            addExpense_label = Label(
                self.add_expense_frame, text="Add Expense", font=("Times New ROman", 20)
            )
            addExpense_label.pack

            username = Label(
                self.add_expense_frame, text="Name: ", font=("Times New Roman", 19)
            )
            username.pack()
            username_entry = Entry(self.add_expense_frame)
            username_entry.pack()

            amountLabel = Label(
                self.add_expense_frame, text="Amount: ", font=("TImes New Roman", 19)
            )
            amountLabel.pack()
            amount_entry = Entry(self.add_expense_frame)
            amount_entry.pack()

            category_label = Label(
                self.add_expense_frame, text="Category: ", font=("Times New Roman", 20)
            )
            category_label.pack()
            category_entry = Entry(self.add_expense_frame)
            category_entry.pack()

            date_label = Label(
                self.add_expense_frame,
                text="Date(YYY-MM-DD)",
                font=("Times New Roman", 20),
            )
            date_label.pack()
            date_entry = Entry(self.add_expense_frame)
            date_entry.pack()

            def add_expenses():
                name = username_entry.get()
                amount = amount_entry.get()
                category = category_entry.get()
                date = date_entry.get()
                self.expense_manager.add_expenses(name, amount, category, date)
                box.showinfo("Success", "Expenses have been added succesfully")

                # Checking if the amount entered is a digit
                if not amount.isdigit():
                    box.showerror("Error", "Amount must be a number!")
                    return
                # Checking of a date is provided by the user if not, the current date will be displayed
                if not date.strip():
                    date = datetime.now().strftime("%Y-%m-%d")

        addBtn = Button(self.add_expense_frame, text="Add", command=add_expenses)
        addBtn.pack(pady=5)

        backBtn = Button(self.add_expense_frame, text="Back", command=self.main_frame)
        backBtn.pack()

    def view_expenses_screen(self):
        if self.login_frame:
            self.login_frame.destroy()

        expense_frame = Frame(self.window)
        expense_frame.pack(pady=20)

        expense_label = Label(
            expense_frame, text="Your Expenses", font=("Times New Roman", 20)
        )
        expense_label.pack()

        self.window.mainloop()
