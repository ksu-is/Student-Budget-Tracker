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
# Removed previous print function

class BudgetTracker:
    def __init__(self):
        self.income = 0.0
        self.expenses = []

    def adding_income(self, amount: float):
        self.income += amount
        print(f"{Pastel.MINT}✨ Income added! Total Income: ${self.income:.2f}{Pastel.END}")

    def adding_expense(self, description: str, amount: float):
        self.expenses.append((description, amount))
        print(f"{Pastel.SOFT_YELLOW}🛒 Expense added: {description} - ${amount:.2f}{Pastel.END}")

    def total_expenses(self) -> float:
        return sum(amount for _, amount in self.expenses)
        #ran this code and no errors yet so that is a good sign

    def remaining_balance(self) -> float:
        return self.income - self.total_expenses()
    
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


        balence = self.remaining_balance()
        balence_color = Pastel.MINT if balence >= 0 else Pastel.PEACH
        emoji = "🎉" if balence >= 0 else "⚠️"
        print(f"{balence_color}🌿 Remaining Balance: ${balence:.2f} {emoji}{Pastel.END}\n")
        # ran this code and no errors yet so that is a good sign :)


def safe_input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{Pastel.PEACH}⚠️ Invalid number entered. Please enter a valid number.{Pastel.END}")
            return None
        