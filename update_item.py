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


# Function to handle adding a new item category
def add_item_category(items):
    new_category = input("Enter the name of the new item category: ")
    items["item_categories"].append({"name": new_category, "items": []})
    print("Item category '{}' added successfully.".format(new_category))


# Function to handle adding a new item
def add_item(items):
    # Display existing item categories
    print("Existing Item Categories:")
    for index, category in enumerate(items["item_categories"], 1):
        print("Press [{}] for {}".format(index, category["name"]))

    # Prompt user to select an item category
    category_index = int(input("Select the item category: ")) - 1
    category = items["item_categories"][category_index]

    # Prompt user for item details
    new_item_name = input("Enter the name of the new item: ")
    new_item_lifetime = int(input("Enter the item's lifetime in days (optional, enter 0 if not applicable): "))
    new_item_quantity = int(input("Enter the quantity of the item in stock: "))

    # Add the new item to the selected item category
    category["items"].append({"name": new_item_name, "lifetime": new_item_lifetime, "quantity": new_item_quantity})
    print("Item '{}' added to category '{}' successfully.".format(new_item_name, category["name"]))


# Function to handle adding or updating item lifetime
def add_item_lifetime(items):
    # Display existing item categories and their items
    print("Existing Item Categories and Items:")
    for category in items["item_categories"]:
        print("Category:", category["name"])
        for index, item in enumerate(category["items"], 1):
            print("Press [{}] for {}".format(index, item["name"]))

    # Prompt user to select an item category and item
    category_index = int(input("Select the item category: ")) - 1
    item_index = int(input("Select the item: ")) - 1
    item = items["item_categories"][category_index]["items"][item_index]

    # Prompt user to enter the new lifetime of the selected item
    new_lifetime = int(input("Enter the new lifetime of the item in days: "))
    item["lifetime"] = new_lifetime
    print("Lifetime of item '{}' updated successfully.".format(item["name"]))


# Function to handle updating item storage
def update_storage(items):
    # Display existing item categories and their items
    print("Existing Item Categories and Items:")
    for category in items["item_categories"]:
        print("Category:", category["name"])
        for index, item in enumerate(category["items"], 1):
            print("Press [{}] for {}".format(index, item["name"]))

    # Prompt user to select an item category and item
    category_index = int(input("Select the item category: ")) - 1
    item_index = int(input("Select the item: ")) - 1
    item = items["item_categories"][category_index]["items"][item_index]

    # Prompt user to enter the new quantity of the selected item
    new_quantity = int(input("Enter the new quantity of the item in stock: "))
    item["quantity"] = new_quantity
    print("Quantity of item '{}' updated successfully.".format(item["name"]))


# Function to mark an item as 'started using'
def mark_item_started_using(items):
    # Display existing item categories and their items
    print("Existing Item Categories and Items:")
    for category in items["item_categories"]:
        print("Category:", category["name"])
        for index, item in enumerate(category["items"], 1):
            print("Press [{}] for {}".format(index, item["name"]))

    # Prompt user to select an item category and item
    category_index = int(input("Plesae select the item category: ")) - 1
    item_index = int(input("Plese select the item: ")) - 1
    item = items["item_categories"][category_index]["items"][item_index]

    # Mark the selected item as 'started using'
    if "started_using" not in item:
        item["started_using"] = datetime.datetime.now().strftime("%Y-%m-%d")
        print("Item '{}' marked as 'started using' successfully.".format(item["name"]))
    else:
        print("Item '{}' is already marked as 'started using'.".format(item["name"]))


# Function to handle the update item process
def update_item(user, items_file):
    items = load_items(items_file)
    
    while True:
        print("\nWelcome to Update Item meow!")
        print("Please select one from the following options:")
        print("Press [1] to Add Item Category")
        print("Press [2] to Add Item")
        print("Press [3] to Add Item Lifetime")
        print("Press [4] to Update Storage")
        print("Press [A] to Go Back to Account Page")
        print("Press [5] to Mark Item as Start Using")
        print("Press [A] to Go Back to Account Page")
        print("Press [Q] to Quit")

        choice = input("Press here: ")
        if choice == '1':  
            add_item_category(items)
        elif choice == '2':  
            add_item(items)
        elif choice == '3':  
            add_item_lifetime(items)
        elif choice == '4':  
            update_storage(items)
        elif choice == '5':  
            mark_item_started_using(items)
        elif choice == 'A': 
            save_items(items, items_file)
            print("Returning to Account Page...")
            return
        elif choice == 'Q':  
            save_items(items, items_file)
            print("Quitting...")
            quit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    accounts_file = "accounts.json"
    user = {"username": "example_user", "password": "example_password"}  # Dummy user data for testing
    update_item(user, accounts_file)
