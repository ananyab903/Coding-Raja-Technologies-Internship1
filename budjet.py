import json
import os

# Function to load existing data from a file
def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            return json.load(file)
    else:
        return {"income": 0, "expenses": []}

# Function to save data to a file
def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

# Function to add income
def add_income(data):
    income = float(input("Enter income amount: "))
    data["income"] += income
    print(f"Income of ${income} added successfully!")

# Function to add expenses
def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data["expenses"].append({"category": category, "amount": amount})
    print(f"Expense of ${amount} in category '{category}' added successfully!")

# Function to calculate remaining budget
def calculate_budget(data):
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    remaining_budget = data["income"] - total_expenses
    return remaining_budget

# Function to analyze expenses
def analyze_expenses(data):
    expense_categories = set(expense["category"] for expense in data["expenses"])
    
    print("\nExpense Analysis:")
    for category in expense_categories:
        category_total = sum(expense["amount"] for expense in data["expenses"] if expense["category"] == category)
        print(f"{category}: ${category_total}")

# Main function
def main():
    data = load_data()

    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            remaining_budget = calculate_budget(data)
            print(f"\nRemaining Budget: ${remaining_budget}")
        elif choice == "4":
            analyze_expenses(data)
        elif choice == "5":
            save_data(data)
            5
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
