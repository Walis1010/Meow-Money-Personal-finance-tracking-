import json
import datetime


# Function to load existing items from a JSON file
def load_items(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"item_categories": []}


# Function to save updated items to a JSON file
def save_items(items, file_path):
    with open(file_path, 'w') as file:
        json.dump(items, file, indent=4)


# Function to handle viewing finance
def view_finance():

    while True:
        print("\In this page, you can...")
        print("Press [1] to Use Filter")
        print("Press [R] to Return to View Page")
        print("Press [Q] to Quit")

        choice = input("Press here: ")
        if choice == '1':
            print("\nFilter Options:")
            print("Press [1] to View by Week")
            print("Press [2] to View by Month")
            print("Press [3] to View by Year")
            filter_choice = input("Enter your filter choice: ")

            if filter_choice == '1':
                # View by Week
                current_date = datetime.datetime.now()
                start_date = current_date - datetime.timedelta(days=current_date.weekday())
                end_date = start_date + datetime.timedelta(days=6)
                print(f"Viewing finances for the week of {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
                # Implement filter by week functionality
                pass
            elif filter_choice == '2':
                # View by Month
                current_date = datetime.datetime.now()
                start_date = datetime.datetime(current_date.year, current_date.month, 1)
                end_date = datetime.datetime(current_date.year, current_date.month + 1, 1) - datetime.timedelta(days=1)
                print(f"Viewing finances for the month of {start_date.strftime('%Y-%m')} ({end_date.strftime('%d')} days)")
                # Implement filter by month functionality
                pass
            elif filter_choice == '3':
                # View by Year
                current_date = datetime.datetime.now()
                start_date = datetime.datetime(current_date.year, 1, 1)
                end_date = datetime.datetime(current_date.year, 12, 31)
                print(f"Viewing finances for the year of {current_date.year}")
                # Implement filter by year functionality
                pass
            else:
                print("Invalid choice. Please try again.")
        elif choice == 'R':
            return
        elif choice == 'Q':
            quit()
        else:
            print("Invalid choice. Please try again.")


# Function to handle viewing item information
def view_item(items):
    while True:
        print("\nIn this page, you can...")
        print("Press [1] to View Lifetime")
        print("Press [2] to View Storage")
        print("Press [3] to View Items marked 'Started Using'")
        print("Press [R] to Return to Account Page")
        print("Press [Q] to Quit")

        choice = input("Press here: ")
        if choice == '1':
            print("\nView Lifetime:")
            for category in items["item_categories"]:
                for item in category["items"]:
                    print(f"Item Name: {item['name']}")
                    print(f"Date Started Using: {item.get('date_started_using', 'Not available')}")
                    print(f"Estimated End Date: {item.get('estimated_end_date', 'Not available')}")
        elif choice == '2':
            print("\nView Storage:")
            for category in items["item_categories"]:
                for item in category["items"]:
                    print(f"Item Type: {category['name']}")
                    print(f"Quantity in Stock: {item['quantity']}")
        elif choice == '3':
            print("\nView Items marked 'Started Using':")
            for category in items["item_categories"]:
                for item in category["items"]:
                    print(f"Item Name: {item['name']}")
                    print(f"Date Started Using: {item.get('date_started_using', 'Not available')}")
                    print(f"Estimated End Date: {item.get('estimated_end_date', 'Not available')}")
        elif choice == 'R':
            return
        elif choice == 'Q':
            quit()
        else:
            print("Invalid choice. Please try again.")


# Function to handle the view options
def view(user, items_file):
    items = load_items(items_file)

    balance = 0
    total_income = 0
    total_expense = 0

    print("Welcome to View Finance meow!")
    print(f"Balance: ${balance}")
    print(f"Total Income: ${total_income}")
    print(f"Total Expense: ${total_expense}")
    
    while True:
        print("\nWelcome to View meow!")
        print("If you want to proceed, please select one from the following ooptions:")
        print("Press [1] to View Finance")
        print("Press [2] to View Item")
        print("Press [A] to Go Back to Account Page")
        print("Press [Q] to Quit")

        choice = input("Press here: ")
        if choice == '1':
            view_finance()
        elif choice == '2':
            view_item()
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
    user = {"username": "example_user", "password": "example_password"}  # Dummy user data for testing
    view(user, accounts_file)
