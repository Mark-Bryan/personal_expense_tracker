from tkinter import *
import tkinter.messagebox as box
from app.main import Authentication
import os
from datetime import datetime
from models.manager import ExpenseManager


class ExpenseTracker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Personal Expense Tracker")
        self.window.geometry("400x500")
        self.main = Authentication()
        self.current_user = None
        self.user_file = "tools/users.json"
        self.expense_file = (
            f"{self.current_user}_expenses.json"
            if self.current_user
            else "expenses.json"
        )
        self.expense_manager = ExpenseManager(self.expense_file)

        self.login_frame = None
        self.register_frame = None
        self.main_frame = None
        self.current_window = None
        self.dark_mode = False

        self.initialise_user_screen()
        self.main_menu()

        self.toggle_button = Button(
            self.window, text="Toogle Dark Mode", command=self.toggle_dark_mode
        )
        self.toggle_button.pack(pady=5)

    def initialise_user_screen(self):
        """Initialises the user file if it doesn't exist"""
        if not os.path.exists(self.user_file):
            print(
                f"The user file '{self.user_file} 'does not exist. Please create it manually"
            )

    def main_menu(self):
        main_label = Label(
            self.window, text="Welcome to Expense Tracker", font=("Times New Roman", 18)
        )
        main_label.pack(padx=20)

        log_btn = Button(self.window, text="Login", command=self.login_screen)
        log_btn.pack(pady=10)

        reg_btn = Button(self.window, text="Register", command=self.register_screen)
        reg_btn.pack(pady=10)

        close_btn = Button(
            self.window, text="Close Application", command=self.close_application
        )
        close_btn.pack(pady=5)

    def register_screen(self):

        if self.current_window:
            self.current_window.destroy()

        self.current_window = Toplevel(self.window)
        self.current_window.title("Register Carefully With Your Credentials")

        reg_label = Label(
            self.current_window, text="Register", font=("Times New Roman", 18)
        )
        reg_label.pack()

        fullname_label = Label(self.current_window, text="Full Name:")
        full_name_entry = Entry(self.current_window)
        fullname_label.pack()
        full_name_entry.pack()

        username_label = Label(self.current_window, text="Username:")
        username_entry = Entry(self.current_window)
        username_label.pack()
        username_entry.pack()

        pd_label = Label(self.current_window, text="Password")
        pd_label.pack()
        pd_entry = Entry(self.current_window, show="*")
        pd_entry.pack()

        def register():
            full_name = full_name_entry.get().strip()
            username = username_entry.get().strip()
            password = pd_entry.get().strip()

            if not full_name.strip() or not username.strip() or not password.strip():
                box.showerror("Error", "Username and password cannot be empty")
                return
            if self.main.register_user(full_name, username, password):
                box.showinfo("Success", "Registration successful. Please log in")
                self.login_screen()
            else:
                box.showerror("Error", "Username already exists. Try a different one")

        reg_btn = Button(self.current_window, text="Register", command=register)
        reg_btn.pack()
        lgnI_btn = Button(
            self.current_window, text="Back To Login", command=self.login_screen
        )
        lgnI_btn.pack()

    def login_screen(self):
        """Shows the login screen"""
        if self.current_window:
            self.current_window.destroy()
        self.current_window = Toplevel(self.window)
        self.current_window.title("Welcome, Log In Your Information To Proceed")

        login_label = Label(
            self.current_window, text="Login", font=("Times New Roman", 18)
        )
        login_label.pack()

        name_label = Label(self.current_window, text="Username: ")
        name_label.pack()

        username_entry = Entry(self.current_window)
        username_entry.pack()

        pwd_label = Label(self.current_window, text="Password: ")
        pwd_entry = Entry(self.current_window, show="*")
        pwd_entry.pack()
        pwd_label.pack()

        def login():
            username = username_entry.get()
            password = pwd_entry.get()

            if self.main.authenticate_user(username, password):
                self.current_user = username
                box.showinfo("Success", f"Welcome, {username}")
                self.main_screen()
            else:
                box.showerror("Error", "Invalid username or password")

        login_btn = Button(self.current_window, text="LogIn", command=login)
        login_btn.pack(pady=5)

        reg_btn = Button(
            self.current_window, text="Register", command=self.register_screen
        )
        reg_btn.pack()

    def main_screen(self):
        """Shows the main screen after login"""
        if self.current_window:
            self.current_window.destroy()

        self.current_window = Toplevel(self.window)
        self.current_window.title("Main Screen")

        wlcLabel = Label(
            self.current_window,
            text=f"Welcome, {self.current_user}",
            font=("Times New Roman", 18),
        )
        wlcLabel.pack()

        addExp_Btn = Button(
            self.current_window, text="Add Expense", command=self.add_expenses
        )
        addExp_Btn.pack(pady=5)

        check_button = Button(
            self.current_window,
            text="Check Expenses",
            command=self.view_expenses_screen,
        )
        check_button.pack(padx=5)

        logOut_btn = Button(self.current_window, text="Log Out", command=self.main_menu)
        logOut_btn.pack(pady=5)

    def add_expenses(self):

        def open_expense_window():
            expense_window = Toplevel(self.window)
            expense_window.title("Add Expense")

            name_label = Label(
                expense_window, text="Name: ", font=("Times New Roman", 20)
            )
            name_label.pack()
            name_entry = Entry(expense_window)
            name_entry.pack()

            amountLabel = Label(
                expense_window, text="Amount: ", font=("Times New Roman", 20)
            )
            amountLabel.pack()
            amount_entry = Entry(expense_window)
            amount_entry.pack()

            category_label = Label(
                expense_window, text="Category: ", font=("Times New Roman", 20)
            )
            category_label.pack()
            category_entry = Entry(expense_window)
            category_entry.pack()

            date_label = Label(
                expense_window,
                text="Date(YYY-MM-DD)",
                font=("Times New Roman", 20),
            )
            date_label.pack()
            date_entry = Entry(expense_window)
            date_entry.pack()

            def save_expenses():
                name = name_entry.get().strip()
                amount = amount_entry.get().strip()
                category = category_entry.get().strip()
                date = date_entry.get().strip()

                # Checking if the amount entered is a digit
                if not amount.isdigit():
                    box.showerror("Error", "Amount must be a number!")
                else:
                    if not name:
                        box.showerror("Error", "Name is required")
                    elif not category:
                        box.showerror("Error", "Category is required")

                    else:
                        ExpenseManager().add_expenses(name, int(amount), category, date)
                        box.showinfo("Success", "Expense added succesfully")
                        expense_window.destroy()

                        if box.askyesno(
                            "Add another ", "Do you want to add another expense?"
                        ):
                            open_expense_window()

            addBtn = Button(expense_window, text="Save", command=save_expenses)
            addBtn.pack(pady=5)

            backBtn = Button(
                expense_window, text="Back", command=expense_window.destroy
            )
            backBtn.pack(pady=5)

        open_expense_window()

    def view_expenses_screen(self):

        view_expense_window = Toplevel(self.window)
        view_expense_window.title("View Your Expenses")

        expense_frame = Frame(view_expense_window)
        expense_frame.pack(pady=20)

        expense_label = Label(
            view_expense_window, text="Your Expenses", font=("Times New Roman", 20)
        )
        expense_label.pack()

        expenses = self.expense_manager.retrieve_expenses()

        if expenses is None:
            box.showerror("Error", "Failed to load expenses")
        else:
            if not expenses:
                exp_label = Label(expense_frame, text="No expenses recorded.")
                exp_label.pack()

            else:
                for expense in expenses:
                    ep_label = Label(
                        expense_frame,
                        text=f"{expense['name']} - {expense['amount']} ({expense['category']}, {expense['date']})",
                    )
                    ep_label.pack()

        bck_btn = Button(view_expense_window, text="Back", command=self.main_screen)
        bck_btn.pack(pady=10)

    def logout(self, main_window=None):
        """Logs the user out and returns to the login screen"""
        self.current_user = None
        if main_window:
            main_window.destroy()
        self.login_screen()

    def clear_window(self):
        if self.login_screen:
            self.login_screen.destroy()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.apply_dark_mode()
        else:
            self.apply_light_mode()

    def apply_dark_mode(self):
        self.window.configure(bg="#2e2e2e")
        self.toggle_button.configure(bg="#444444", fg="#ffffff")

        self.configure_frame(self.login_frame, "#2e2e2e", "#ffffff")
        self.configure_frame(self.register_frame, "#2e2e2e", "#ffffff")
        self.configure_frame(self.main_frame, "#2e2e2e", "#ffffff")

    def apply_light_mode(self):
        self.window.configure(bg="#ffffff")
        self.toggle_button.configure(bg="#f0f0f0", fg="#000000")

        self.configure_frame(self.login_frame, "#ffffff", "#2e2e2e")
        self.configure_frame(self.register_frame, "#ffffff", "#2e2e2e")
        self.configure_frame(self.main_frame, "#ffffff", "#2e2e2e")

    def configure_frame(self, frame, bg_color, fg_color):
        if frame and frame.winfo_exists():
            frame.configure(bg=bg_color)
            for widget in frame.winfo_children():
                if widget.winfo_exists():
                    widget.configure(bg=bg_color, fg=fg_color)

    def close_application(self):
        if box.askyesno("Exit", "Are you sure you would like to close the application"):
            self.window.destroy()


ExpenseTracker().window.mainloop()
