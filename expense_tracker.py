import json
import os

EXPENSES_FILE = "expenses.json"


def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    expense = {
        "date": date,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return

    try:
        index = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted_expense = expenses.pop(index)
            print(f"Deleted expense: {deleted_expense}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Save and Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Expenses saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
