import json


# Function to load existing accounts from a JSON file
def load_accounts(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"accounts": []}


# Function to save updated accounts to a JSON file
def save_accounts(accounts, file_path):
    with open(file_path, 'w') as file:
        json.dump(accounts, file, indent=4)


# Function to handle user registration
def register(accounts):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username is already taken
    for account in accounts["accounts"]:
        if account["username"] == username:
            print("Username already exists. Please choose a different username.")
            return

    # Add the new account
    accounts["accounts"].append({"username": username, "password": password})
    save_accounts(accounts, "accounts.json")
    print("Registration successful.")


# Function to handle user login
def login(accounts):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    for account in accounts["accounts"]:
        if account["username"] == username and account["password"] == password:
            print("Login successful.")
            return True
    print("Incorrect username or password. Please try again.")
    return False


# Function to handle the main execution
def main():
    accounts = load_accounts("accounts.json")
    while True:
        print("\nWelcome to Meow Money!")
        print("Press [1] to Register")
        print("Press [2] to Login")
        print("Press [Q] to Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            register(accounts)
        elif choice == '2':
            if login(accounts):
                # Call the function to provide user options after login
                pass  # Placeholder for future implementation
        elif choice == 'Q':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
