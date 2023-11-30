# A simple to do list program

# Define a list to store the items
todo_list = []

# Define a function to load the list from a file
def load_list():
    global todo_list
    try:
        # Open the file in read mode
        with open("todo_list.txt", "r") as f:
            # Read each line and append it to the list
            for line in f:
                todo_list.append(line.strip())
    except FileNotFoundError:
        # If the file does not exist, create an empty file
        with open("todo_list.txt", "w") as f:
            pass

# Define a function to save the list to a file
def save_list():
    global todo_list
    # Open the file in write mode
    with open("todo_list.txt", "w") as f:
        # Write each item in the list to a new line
        for item in todo_list:
            f.write(item + "\n")

# Define a function to display the list
def display_list():
    global todo_list
    # Check if the list is empty
    if len(todo_list) == 0:
        print("Your to do list is empty.")
    else:
        # Print the list with numbers
        print("Your to do list:")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}")

# Define a function to add an item to the list
def add_item():
    global todo_list
    # Prompt the user for the item
    item = input("Enter the item you want to add: ")
    # Append the item to the list
    todo_list.append(item)
    # Save the list to the file
    save_list()
    # Print a confirmation message
    print(f"{item} has been added to your to do list.")

# Define a function to remove an item from the list
def remove_item():
    global todo_list
    # Check if the list is empty
    if len(todo_list) == 0:
        print("Your to do list is empty. Nothing to remove.")
    else:
        # Display the list with numbers
        display_list()
        # Prompt the user for the number of the item
        num = input("Enter the number of the item you want to remove: ")
        # Validate the input
        try:
            # Convert the input to an integer
            num = int(num)
            # Check if the number is valid
            if num < 1 or num > len(todo_list):
                print("Invalid number. Please try again.")
            else:
                # Remove the item from the list
                item = todo_list.pop(num - 1)
                # Save the list to the file
                save_list()
                # Print a confirmation message
                print(f"{item} has been removed from your to do list.")
        except ValueError:
            # If the input is not an integer, print an error message
            print("Invalid input. Please enter a number.")

# Define a function to edit an item in the list
def edit_item():
    global todo_list
    # Check if the list is empty
    if len(todo_list) == 0:
        print("Your to do list is empty. Nothing to edit.")
    else:
        # Display the list with numbers
        display_list()
        # Prompt the user for the number of the item
        num = input("Enter the number of the item you want to edit: ")
        # Validate the input
        try:
            # Convert the input to an integer
            num = int(num)
            # Check if the number is valid
            if num < 1 or num > len(todo_list):
                print("Invalid number. Please try again.")
            else:
                # Get the old item from the list
                old_item = todo_list[num - 1]
                # Prompt the user for the new item
                new_item = input(f"Enter the new item for {old_item}: ")
                # Replace the old item with the new item in the list
                todo_list[num - 1] = new_item
                # Save the list to the file
                save_list()
                # Print a confirmation message
                print(f"{old_item} has been changed to {new_item} in your to do list.")
        except ValueError:
            # If the input is not an integer, print an error message
            print("Invalid input. Please enter a number.")

# Define a function to display the menu
def display_menu():
    # Print the menu options
    print("To do list program")
    print("Please choose an option:")
    print("1. View your to do list")
    print("2. Add an item to your to do list")
    print("3. Remove an item from your to do list")
    print("4. Edit an item in your to do list")
    print("5. Exit the program")

# Define a function to execute the menu
def execute_menu():
    # Display the menu
    display_menu()
    # Prompt the user for the option
    option = input("Enter your option: ")
    # Validate the input
    try:
        # Convert the input to an integer
        option = int(option)
        # Check if the option is valid
        if option < 1 or option > 5:
            print("Invalid option. Please try again.")
        else:
            # Execute the corresponding function
            if option == 1:
                display_list()
            elif option == 2:
                add_item()
            elif option == 3:
                remove_item()
            elif option == 4:
                edit_item()
            elif option == 5:
                print("Thank you for using the to do list program. Goodbye!")
                return
    except ValueError:
        # If the input is not an integer, print an error message
        print("Invalid input. Please enter a number.")
    # Ask the user if they want to continue
    answer = input("Do you want to continue? (y/n): ")
    # Validate the input
    if answer.lower() == "y":
        # Execute the menu again
        execute_menu()
    elif answer.lower() == "n":
        print("Thank you for using the to do list program. Goodbye!")
        return
    else:
        print("Invalid input. Please enter y or n.")

# Load the list from the file
load_list()
# Execute the menu
execute_menu()
