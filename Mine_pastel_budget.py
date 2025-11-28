# So this will be the begining of the creating a aesthetic  budget tracker for everyone but students
# for the colors I was thinking of using pastel colors to make it more visually appealing

class Pastel:
    PINK = "\033[95m"
    MINT = "\033[96m"
    LAVENDER = "\033[94m"
    PEACH = "\033[91m"
    SOFT_YELLOW = "\033[93m"
    END = "\033[0m"
    BOLD = "\033[1m"
    # Initializing the Pastel class with color codes
    # I ran this code and no errors yet so that is a good sign :)

# I want to add some sort of art, maybe an ASCI art banner
BANNER = f"""
{Pastel.PINK}{Pastel.BOLD}
   ╔════════════════════════════════════════════╗
   ║        🎀  BUDGET TRACKER  🎀              ║
   ╚════════════════════════════════════════════╝
{Pastel.END}
"""
# Ran this code and no errors yet so that is a good sign :)
# I was hoping to see it but I realized I forgot to add the print function to see it.
# Banner looks great after adding the print function
# Removed previous "print" function

class BudgetTracker:
    def __init__(self):
        self.income = 0.0
        self.expenses = []
# Initializing the BudgetTracker class with income and expenses attributes

    def adding_income(self, amount: float):
        self.income += amount
        print(f"{Pastel.MINT}✨ Income added! Total Income: ${self.income:.2f}{Pastel.END}")
# Defining the function to add income
# Will print out the total income after adding the new amount with a sparkle emoji

    def adding_expense(self, description: str, amount: float):
        self.expenses.append((description, amount))
        print(f"{Pastel.SOFT_YELLOW}🛒 Expense added: {description} - ${amount:.2f}{Pastel.END}")
# Def ining the function to add expenses
# Will print out the description and amount of the expense added, a shopping cart emoji, and a description of the expense added

    def total_expenses(self) -> float:
        return sum(amount for _, amount in self.expenses)
        #ran this code and no errors yet so that is a good sign

    def remaining_balance(self) -> float:
        return self.income - self.total_expenses()
    # This function will calculate the remaining balance by subtracting total expenses from income

    
    def display_summary(self):
        print(f"\n{Pastel.LAVENDER}{Pastel.BOLD}💼  Budget Summary  💼{Pastel.END}")
        print(f"{Pastel.MINT}💵 Total Income: ${self.income:.2f}{Pastel.END}")
        print(f"{Pastel.PINK}📘 Expenses:{Pastel.END}")
        if not self.expenses:
            print(f"{Pastel.PEACH}  (No expenses recorded yet).{Pastel.END}")
        else:
            for descrpt, amnt in self.expenses:
                print(f"{Pastel.PEACH}   • {descrpt}: ${amnt:.2f} 🧾{Pastel.END}")
        print(f"{Pastel.LAVENDER}📊 Total Expense: ${self.total_expenses():.2f}{Pastel.END}")
# this function will display the summary of the budget
# the if else statement will check if there are any expenses recorded yet
# Will print expenses if there are any

        balence = self.remaining_balance()
        balence_color = Pastel.MINT if balence >= 0 else Pastel.PEACH
        emoji = "🎉" if balence >= 0 else "⚠️"
        print(f"{balence_color}🌿 Remaining Balance: ${balence:.2f} {emoji}{Pastel.END}\n")
        # ran this code and no errors yet so that is a good sign :)
        # Defined balence variable to store the remaining balance
        # Defined balance_color and emoji variables for better readability
        # This will print the remaining balance with a different color and emoji based on whether it's positive or negative


def safe_input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{Pastel.PEACH}⚠️ Invalid number entered. Please enter a valid number.{Pastel.END}")
            return None
        # This coded loop will keep asking until a valid float is entered.
        # Ran the code with the "while True" loop so hopeful that is a good sign. This is my first time using it.


if __name__ == "__main__":
    print (BANNER)
    print (f"{Pastel.LAVENDER}Welcome to the your Budget Tracker! 🌈✨{Pastel.END}")