import json
import datetime

# Function to load existing accounts from a JSON file
def load_accounts(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

# Function to save updated accounts to a JSON file
def save_accounts(accounts, file_path):
    with open(file_path, 'w') as file:
        json.dump(accounts, file, indent=4)

# Function to handle updating finance information
def update_finance(user, accounts_file):
    while True:
        print("\nWelcome to Update Finance meow!")
        print("Please select one from the following options:")
        print("Press [1] to Add Income Type")
        print("Press [2] to Add Expense Type")
        print("Press [3] to Add Income")
        print("Press [4] to Add Expense")
        print("Press [5] to Remove Type")
        print("Press [A] to Go Back to Account Page")
        print("Press [Q] to Quit")

        choice = input("Press here: ").upper()
        if choice == '1':  
            new_income_type = input("Please enter the name of the new income type: ")
            user['income_types'].append(new_income_type)
            print("Income type added successfully.")
        elif choice == '2':  
            new_expense_type = input("Please enter the name of the new expense type: ")
            user['expense_types'].append(new_expense_type)
            print("Expense type added successfully.")
        elif choice == '3': 
            if len(user['income_types']) == 0:
                print("Please add an income type first.")
                continue
            print("Please select an income type:")
            for i, income_type in enumerate(user['income_types']):
                print(f"{i + 1}. {income_type}")
            income_type_index = int(input("Enter the index of the income type: ")) - 1
            income_amount = float(input("Enter the amount of income: "))
            user['total_income'] += income_amount
            user['income'][user['income_types'][income_type_index]] = income_amount
            print("Income added successfully.")
        elif choice == '4': 
            if len(user['expense_types']) == 0:
                print("Please add an expense type first.")
                continue
            print("Please select an expense type:")
            for i, expense_type in enumerate(user['expense_types']):
                print(f"{i + 1}. {expense_type}")
            expense_type_index = int(input("Enter the index of the expense type: ")) - 1
            expense_amount = float(input("Enter the amount of expense: "))
            user['total_expense'] += expense_amount
            user['expense'][user['expense_types'][expense_type_index]] = expense_amount
            print("Expense added successfully.")
        elif choice == '5':  
            print("Which type do you want to remove?")
            print("1. Income Type")
            print("2. Expense Type")
            remove_choice = input("Please enter your choice: ")
            if remove_choice == '1':
                print("Please select an income type to remove:")
                for i, income_type in enumerate(user['income_types']):
                    print(f"{i + 1}. {income_type}")
                remove_index = int(input("Please enter the index of the income type: ")) - 1
                removed_income_type = user['income_types'].pop(remove_index)
                del user['income'][removed_income_type]
                print(f"Income type '{removed_income_type}' removed successfully.")
            elif remove_choice == '2':
                print("Please select an expense type to remove:")
                for i, expense_type in enumerate(user['expense_types']):
                    print(f"{i + 1}. {expense_type}")
                remove_index = int(input("PLease enter the index of the expense type: ")) - 1
                removed_expense_type = user['expense_types'].pop(remove_index)
                del user['expense'][removed_expense_type]
                print(f"Expense type '{removed_expense_type}' removed successfully.")
            else:
                print("Invalid choice.")
        elif choice == 'A':  
            print("Returning to Account Page...")
            return
        elif choice == 'Q':  
            print("Quitting...")
            quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    accounts_file = "accounts.json"
    user = {"username": "example_user", "password": "example_password", "income_types": [], "expense_types": [], "income": {}, "expense": {}, "total_income": 0, "total_expense": 0}  # Dummy user data for testing
    update_finance(user, accounts_file)
