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
        self.budget = 0.0
        self.expenses = []

    def adding_income(self, amount: float):
        self.budget += amount
        print(f"{Pastel.MINT} Income added! Total Income: ${self.income:.2f}{Pastel.END}")

    def adding_expense(self, description: str, amount: float):
        self.expenses.append((description, amount))
        print(f"{Pastel.SOFT_YELLOW}🛒 Expense added: {description} - ${amount:.2f}{Pastel.END}")


