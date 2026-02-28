import json
import hashlib

def Authentication(username: str, password : str):
     with open("database.json", "r") as f:
        data = json.load(f)
    
     for user in data["users"]:
        if user["username"] == username:
            if user["password"] == password:
                return "Login successful"
            else:
                return "Incorrect password"
    
     return "Username not found, perhaps its a typo?"
     
def Register(username: str, password: str, balance: float):
    with open("database.json", "r") as f:
        data = json.load(f)

    for user in data["users"]:
        if user["username"] == username:
            return "Username already exists"
        
    data["users"].append({"username": username, "password": password, "balance": balance})

    with open("database.json", "w") as f:
        json.dump(data, f, indent=2)
    
    return "Registration successful"


def show_balance(username : str):
    with open("database.json", "r") as f:
        data = json.load(f)
    for user in data["users"]:
        if user["username"] == username:
            print(f"Your balance is {user['balance']}")

def deposit( username: str, amount: float):
    with open("database.json", "r") as f:
        data = json.load(f)
    data["balance"] += amount
    with open("database.json", "w") as f:
        json.dump(data, f, indent=2)
    return

def withdraw(username: str, amount: float):
    with open("database.json", "r") as f:
        data = json.load(f)
    if data["balance"] >= amount:
        data["balance"] -= amount
        with open("database.json", "w") as f:
            json.dump(data, f, indent=2)
        return "Amount withdrawn successfully"
    else:
        return "Insufficient balance"
    
def transfer(sender: str, receiver: str, amount: float):
    with open("database.json", "r") as f:
        data = json.load(f)
    
    if sender == receiver:
        return "You cannot transfer to yourself"
    
    sender_account = None
    receiver_account = None
    
    for user in data["users"]:
        if user["username"] == sender:
            sender_account = user
        if user["username"] == receiver:
            receiver_account = user
    
    if receiver_account is None:
        return "Receiver not found"
    
    if sender_account["balance"] >= amount:
        sender_account["balance"] -= amount
        receiver_account["balance"] += amount
        with open("database.json", "w") as f:
            json.dump(data, f, indent=2)
        return "Amount transferred successfully"
    else:
        return "Transfer failed, insufficient balance"


#------------------------------------------------------------------------------





print("------------Welcome to the Celestial Jr------------")

while True:
    choice = input("Enter 1 to login || Enter 2 to register || Enter 3 to exit: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice, please enter 1, 2 or 3")
        continue

    if choice == "3":
        print("Goodbye!")
        break

    if choice == "1":
        username = input("Enter your username: ").strip()
        if username == "":
            print("Username cannot be empty")
            continue

        password = input("Enter your password: ").strip()
        if password == "":
            print("Password cannot be empty")
            continue

        result = Authentication(username, password)
        print(result)

        if result == "Login successful":
            while True:
                switch = input("Enter 1 to show balance || Enter 2 to deposit || Enter 3 to withdraw || Enter 4 to transfer || Enter 5 to logout: ")

                if switch not in ["1", "2", "3", "4", "5"]:
                    print("Invalid choice, please enter 1, 2, 3, 4 or 5")
                    continue

                if switch == "5":
                    print("Logged out successfully")
                    break
                elif switch == "1":                                     #BALANCE CHECK
                    show_balance(username)
                elif switch == "2":                                     #DEPOSIT CHECK
                    try:
                        amount = float(input("Enter the amount you want to deposit: "))
                        if amount <= 0:
                            print("Amount must be greater than 0")
                            continue
                        print(deposit(username, amount))
                    except ValueError:
                        print("Invalid amount, please enter a number")
                elif switch == "3":                                     #WITHDRAW CHECK
                    try:
                        amount = float(input("Enter the amount you want to withdraw: "))
                        if amount <= 0:
                            print("Amount must be greater than 0")
                            continue
                        print(withdraw(username,amount))
                    except ValueError:
                        print("Invalid amount, please enter a number")
                elif switch == "4":                                     #TRANSFER CHECK
                    receiver = input("Enter the username of the receiver: ")
                    if not receiver.strip():
                        print("Receiver username cannot be empty")
                        continue
                    try:
                        amount = float(input("Enter the amount you want to transfer: "))
                        if amount <= 0:
                            print("Amount must be greater than 0")
                            continue
                        print(transfer(username, receiver, amount))
                    except ValueError:
                        print("Invalid amount, please enter a number")

    elif choice == "2":
        username = input("Enter your username: ").strip()
        if username == "":
            print("Username cannot be empty")
            continue

        password = input("Enter your password: ").strip()
        if password == "":
            print("Password cannot be empty")
            continue

        try:
            balance = float(input("Enter your starting balance: "))
            if balance < 0:
                print("Balance cannot be negative")
                continue
            print(Register(username, password, balance))
        except ValueError:
            print("Invalid balance, please enter a number")

    







