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

# Function to handle the login process
def login(accounts_file):
    # Load existing accounts
    accounts = load_accounts(accounts_file)
    
    # Display the main menu
    print("Welcome to Meow Money! Please...")
    print("Press [1] to login")
    print("Press [2] to register")
    print("Press [q] to quit")
    
    # Get user choice
    choice = input("Press here: ")
    if choice == '1':  # Login
        while True:
            # Prompt user for username
            username = input("Please enter your username: ")
            # Check if username exists
            if not any(user['username'] == username for user in accounts['users']):
                print("Username not found. Please try again or register.")
                continue
            
            # Get user details
            user = next(user for user in accounts['users'] if user['username'] == username)
            
            # Prompt user for password
            for _ in range(10):  # 10 attempts
                password = input("Please enter your password: ")
                # Check if password is correct
                if bcrypt.checkpw(password.encode(), user['password'].encode()):
                    print("Login successful.")
                    return user
                else:
                    print("Incorrect password. Please try again.")
            print("Too many incorrect attempts. Meowy is terminating the program for everyone's safety.")
            print("You can run the programme again 5 minutes.")
            sleep(300)
            quit()
    elif choice == '2':  # Register
        # Implement registration functionality
        pass
    elif choice == '3':  # Quit
        quit()
    else:
        print("Invalid choice. Please try again.")
        login(accounts_file)

# Main entry point
if __name__ == "__main__":
    accounts_file = "accounts.json"
    user = login(accounts_file)
    print("User:", user)