import datetime
import json

# Initialize transactions list
transactions = []

# Data structure for transactions
class Transaction:
    def __init__(self, date, amount, category, transaction_type):
        self.date = date
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

# Function to display menu options
def display_menu():
    print("\nBudget Tracker Menu:")
    print("1. Add expense")
    print("2. Add income")
    print("3. View transactions")
    print("4. Analyze expenses")
    print("5. Set budget")
    print("6. View budget summary")
    print("7. Save data")
    print("8. Load data")
    print("9. Exit")
    choice = input("Enter your choice: ")
    return choice

# Function to add a transaction
def add_transaction():
    date_str = input("Enter date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    transaction_type = input("Enter type (income/expense): ").lower()
    transaction = Transaction(date, amount, category, transaction_type)
    transactions.append(transaction)
    print("Transaction added successfully!")

# Function to view transactions
def view_transactions():
    print("\nTransactions:")
    for transaction in transactions:
        print(f"{transaction.date.strftime('%Y-%m-%d')}: {transaction.transaction_type.capitalize()} - {transaction.category} - ${transaction.amount:.2f}")

# Function to analyze expenses
def analyze_expenses():
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    filtered_transactions = [t for t in transactions if t.date >= start_date and t.date <= end_date and t.transaction_type == "expense"]

    total_expense = sum(t.amount for t in filtered_transactions)
    category_totals = {}
    for transaction in filtered_transactions:
        category_totals[transaction.category] = category_totals.get(transaction.category, 0) + transaction.amount

    # Display analysis
    print("\nExpense Analysis:")
    print(f"Total Expenses: ${total_expense:.2f}")
    for category, amount in category_totals.items():
        print(f"- {category}: ${amount:.2f}")

# Function to set budget
def set_budget():
    global monthly_budget
    monthly_budget = float(input("Enter monthly budget: "))
    print("Budget set successfully!")

# Function to view budget summary
def view_budget_summary():
    if not monthly_budget:
        print("Please set a budget first.")
        return

    # Calculate current month and expenses
    today = datetime.date.today()
    current_month_expenses = sum(t.amount for t in transactions if t.date.year == today.year and t.date.month == today.month and t.transaction_type == "expense")

    # Calculate remaining budget and percentage spent
    remaining_budget = monthly_budget - current_month_expenses
    percent_spent = current_month_expenses / monthly_budget * 100

    print("\nBudget Summary:")
    print(f"Monthly Budget: ${monthly_budget:.2f}")
    print(f"Current Month Expenses: ${current_month_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    print(f"Percent Spent: {percent_spent:.2f}%")

# Function to save data
def save_data():
    with open("data.json", "w") as f:
        json.dump([vars(transaction) for transaction in transactions], f, default=str)
    print("Data saved successfully!")

# Function to load data
def load_data():
    try:
        with open("data.json", "r") as f:
            global transactions
            data = json.load(f)
            transactions = [Transaction(datetime.datetime.fromisoformat(t['date']), t['amount'], t['category'], t['transaction_type']) for t in data]
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found.")

# Main program loop
monthly_budget = None
while True:
    choice = display_menu()
    if choice == "1":
        add_transaction()
    elif choice == "2":
        add_transaction()
    elif choice == "3":
        view_transactions()
    elif choice == "4":
        analyze_expenses()
    elif choice == "5":
        set_budget()
    elif choice == "6":
        view_budget_summary()
    elif choice == "7":
        save_data()
    elif choice == "8":
        load_data()
    elif choice == "9":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 9.")
