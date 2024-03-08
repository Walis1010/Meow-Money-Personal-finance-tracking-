import json
import bcrypt
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


# Function to handle the account settings
def account_settings(user, accounts_file):
    while True:
        print("\nWelcome to the Account Settings meow!")
        print("Please select one from the following options:")
        print("Press [1] to Change Username")
        print("Press [2] to Change Password")
        print("Press [3] to View Account Info")
        print("Press [A] to Go Back to Account Page")
        print("Press [Q] to Quit")
        
        choice = input("Press here: ").upper()
        if choice == '1':  # Change Username
            current_password = input("Enter your current password: ")
            if bcrypt.checkpw(current_password.encode(), user['password'].encode()):
                new_username = input("Enter your new username: ")
                user['username'] = new_username
                print("Username changed successfully.")
            else:
                print("Incorrect password. Username change failed.")
        elif choice == '2':  # Change Password
            current_password = input("Enter your current password: ")
            if bcrypt.checkpw(current_password.encode(), user['password'].encode()):
                new_password = input("Enter your new password: ")
                hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
                user['password'] = hashed_password
                print("Password changed successfully.")
            else:
                print("Incorrect password. Password change failed.")
        elif choice == '3':  # View Account Info
            print("Current Username: {}".format(user['username']))
            print("Account Creation Date: {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        elif choice == 'A':  # Quit
            print("Returning to Account Page...")
            return
        elif choice == 'Q':  # Go Back to Account Page
            print("Quitting...")
            quit()
        else:
            print("Invalid choice. Please try again.")


# Main entry point
if __name__ == "__main__":
    accounts_file = "accounts.json"
    user = {"username": "example_user", "password": "example_password"}  # Dummy user data for testing
    account_settings(user, accounts_file)
