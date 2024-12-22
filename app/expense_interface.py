from tkinter import *
import tkinter.messagebox as box


class ExpenseTracker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Personal Expense Tracker")

        self.current_user = None
        self.login_frame = None
        self.register_frame = None
        self.main_frame = None

    def login_screen(self):
        if self.login_frame:
            self.login_frame.destroy()
        self.login_frame = Frame(self.window)
        self.login_frame.pack(pady=15)

        login_label = Label(self.login_frame, text="Login", font=("Arial", 18))
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
            if self.login_frame:
                self.login_frame.destroy()
            self.register_frame = Frame(self.window)
            self.register_frame.pack(pady=20)

            reg_label = Label(self.register_frame, text="Register", font=("Arial", 18))
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
            if self.login_frame:
                self.login_frame.destroy()
            if self.register_frame:
                self.register_frame.destroy()

            self.main_frame = Frame(self.window)
            self.main_frame.pack(pady=20)

            wlcLabel = Label(
                self.main_frame,
                text=f"Welcome, {self.current_user}",
                font=("Arial", 18),
            )
            wlcLabel.pack()

            def log_out():
                self.current_user = None
                self.main_frame.destroy()
                self.login_screen()

            lgnO_btn = Button(self.main_frame, text="Log Out", command=log_out)
            lgnO_btn.pack()

            self.window.mainloop()
