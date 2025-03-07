import time
import os

Inventory =  {}
user = {}

def add_inventory():
    while True:
        quantity = input("\nEnter the amount of product you want to add to the Inventory: ")
        if quantity.isdigit():
            quatntity_int = int(quantity)
            for i in range(quatntity_int):
                while True:
                    item = input("Enter the item you want to add: ")
                    item_upper = item.upper()
                    if not item_upper.isdigit():
                        string_item = str(item_upper)
                        while True:
                            cost = input("Cost of item: ")
                            if cost.isdigit():
                                cost_int = int(cost)
                                Inventory[string_item] = cost_int
                                print(f'Inventory:\n{Inventory}')
                                break
                            else:
                                print("\nPlease enter the correct value")
                        break
                    else:
                        print("\nPlease enter correct value")
            break
        else:
            print("\nPlease enter the correct value")
            


        
    return main(), Inventory


def remove_item():
    while True:
        select = input("\nEnter the item you want to remove: ")
        select_upper = select.upper()
        if str(select_upper) in Inventory:
            Inventory.pop(select_upper)
            print("Item removed")
            break
        else:
            print("\nItem not in the inventory")
            while True:
                select4 = input("\n1. Would you like to add the item to the inventory\n2. Carry on editing inventory\n3. Go back to Main Menu\nSelect one of the options: ")
                if str(select4) == "1":
                    add_inventory()
                elif str(select4) == "2":
                    break
                elif str(select4) == "3":
                    main()
                    break
                else:
                    print("\nPlease select an appropiate option")


def total_inventory_cost():
    total = sum(Inventory.values())
    print(f'\nTotal value of the inventory: £{total}')

def update_Inventory():
    while True:
        print(f'\nHere is the inventory: \n{Inventory}')
        select2 = input("Enter the item you want to edit: ")
        select2_upper = select2.upper()
        if not select2_upper.isdigit() and select2_upper in Inventory:
            while True:
                select3 = input("Enter the new cost: ")
                if select3.isdigit():
                    select3_int = int(select3)
                    Inventory[select2_upper] = select3_int
                    break
                else:
                    print("\nPlease enter a number")
            break
        else:
            print("\nPlease enter a valid item name")

def save_inventory():
    with open("inventory.txt", "w") as file:
        for item, cost in Inventory.items():
            file.write(f"{item}, {cost}\n")  # Save each item and cost as "Item, cost"
    print("\nInventory has been saved to 'inventory.txt'.")

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                item, cost = line.strip().split(", ")
                Inventory[item] = int(cost)  # Load the item and cost back into the dictionary
        print("\nInventory has been loaded from 'inventory.txt'.")
    except FileNotFoundError:
        print("\nNo saved inventory found.")

def delete_inventory():
    # Check if the inventory.txt file exists
    if os.path.exists("inventory.txt"):
        # Open the file in write mode which will clear its contents
        with open("inventory.txt", "w") as file:
            file.truncate(0)  # Explicitly truncate the file (this clears it)
        

        print("\nInventory has been deleted and 'inventory.txt' has been cleared.")
    else:
        # If the file doesn't exist, print the message
        print("\nFile not found. No inventory to delete.")



def signup():
    print("\nSignup:")
    while True:
        username = input("Enter your desired username (Case sensitive): ")
        if len(username) != 0:
            str_username = str(username)
            while True:
                password = input("Enter your desired password: ")
                if len(password) != 0:
                
                    while True:
                        password_check = input("Please re-enter your password: ")
                        if str(password) == str(password_check):
                            str_password_check = str(password_check)
                            print(f'\nCreated an account for {str_username}')
                            time.sleep(3)
                            user[str_username] = str_password_check
                            print(user)
                            with open("logins.txt", "a") as file:
                                for str_username, str_password_check in user.items():
                                    file.write(f'{str_username}, {str_password_check}\n')
                            login()
                            break
                        else:
                            print("Password incorrect. Retry")
                    break           
                else:
                    print("Please enter a password")
            break
                      
        else:
            print("Please enter a username")
    return user


def login():
    print("\nLogin:")
    while True:
        try:
            with open("logins.txt", "r") as file:
                for line in file:
                    str_username, str_password_check = line.strip().split(", ")
                    user[str_username] = str(str_password_check)  # Load the item and cost back into the dictionary
            print(user)
            while True:
                login_username = input("\nEnter your username (Case sensitive): ")
                login_password = input("Enter your password: ")
                str_login_username = str(login_username)
                str_login_password = str(login_password)
                if str_login_password == user.get(str_login_username):
                    print("\nSuccessful\nLogging in...")
                    time.sleep(3)
                    break
                else:
                    print("Username or password incorrect.")
            break
            



        except FileNotFoundError:
            print("\nNo login found.")
            signup()
        break
        
    return user


def startup_screen():
    print("\nLoading...")
    time.sleep(3)

    while True:
        option_log_sign = input("\n1. Signup\n2. Log in\nSelect one of the following options: ")
        if str(option_log_sign) == "1":
            signup()
            break
        elif str(option_log_sign) == "2":
            login()
            break
        else:
            print("Please select one of the options")


def main():
    print("\nLoading...")
    time.sleep(3)



    while True:
        option = input("\n1. View inventory\n2. Update inventory\n3. Calculate total cost of inventory\n4. Options\n5. Exit\nSelect one of the following options: ")
        if str(option) == "1":
            print(f'\nHere is your inventory: \n{Inventory}')

        elif str(option) == "2":
            while True:
                option2 = input("\n1. Add an item to the inventory\n2. Delete an item in the inventory\n3. Change the cost of an Item\n4. Go back to Main Menu\nSelect one of the following options: ")
                if str(option2) == "1":
                    add_inventory()
                    break
                elif str(option2) == "2":
                    remove_item()
                    break
                elif str(option2) == "3":
                    update_Inventory()
                    break
                elif str(option2) == "4":
                    main()
                    break
                else:
                    print("\nPlease select an appropiate option")

        elif str(option) == "3":
            total_inventory_cost()

        elif str(option) == "4":
            while True:
                option3 = input("\n1. Save inventory\n2. Load inventory\n3. Delete inventory\n4. Go back to Main Menu\nSelect one of the following options: ")
                if str(option3) == "1":
                    save_inventory()
                    break
                elif str(option3) == "2":
                    load_inventory()
                    break
                elif str(option3) == "3":
                    delete_inventory()
                    break
                elif str(option3) == "4":
                    main()
                    break
                else:
                    print("Please selct an appropiate option")

        elif str(option) == "5":
            exit()

        else:
            print("\nPlease select an appropiate option")

print("Welcome to IMS")
startup_screen()
main()