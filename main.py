import json

# File path for storing data
file_name = "data.json"

# Load existing users from the JSON file or start with an empty list
try:
    with open(file_name, "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

# Instructions for the user
print('Instruction:')
print("1: Add user")
print("2: Remove user")
print("3: View users")
print("4: Exit")

# Function to add a user
def addUser(name, occupation):
    users.append({"name": name, "occupation": occupation})
    saveData()

# Function to remove a user
def removeUser(name):
    global users
    users = [user for user in users if user["name"] != name]
    saveData()

# Function to view all users
def viewUser():
    if users:
        print("Current Users:")
        for user in users:
            print(f"Name: {user['name']}, Occupation: {user['occupation']}")
    else:
        print("No users found.")

# Function to save data to the JSON file
def saveData():
    with open(file_name, "w") as file:
        json.dump(users, file, indent=4)
    print("Data saved to file.")

# Main program loop
while True:
    query = int(input("Enter your option number: "))
    if query == 1:
        name = input('Enter your name: ')
        occupation = input('Enter your occupation: ')
        addUser(name, occupation)
    elif query == 2:
        name = input('Enter the user name to remove: ')
        removeUser(name)
    elif query == 3:
        viewUser()
    elif query == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Please enter a valid option number.")
