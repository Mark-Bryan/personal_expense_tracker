class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }
