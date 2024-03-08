import json
import bcrypt


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


def register_account(accounts_file):
    # Load existing accounts
    accounts = load_accounts(accounts_file)
    
    while True:
        # Prompt user for username
        username = input("Enter your username: ")
        # Check if username is already in use
        if any(user['username'] == username for user in accounts['users']):
            print("Username already in use. Please choose a different username.")
            continue
        
        # Confirm the username
        confirm_username = input(f"Confirm username '{username}' (y/n): ")
        if confirm_username.lower() != 'y':
            continue
        
        break
    
    while True:
        # Prompt user for password and hash it
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        
        # Confirm the password
        confirm_password = input("Confirm password (y/n): ")
        if confirm_password.lower() != 'y':
            continue
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        break
    
    # Create a new user account
    new_user = {
        "username": username,
        "password": hashed_password,
        "account_balance": 0,
        "income_types": [],
        "expense_types": [],
        "items": {}
    }
    
    # Add the new user to the accounts data and save it
    accounts['users'].append(new_user)
    save_accounts(accounts, accounts_file)
    print("Account created successfully.")


# Main entry point
if __name__ == "__main__":
    accounts_file = "accounts.json"
    register_account(accounts_file)