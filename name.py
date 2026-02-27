# TASK: Write a function that shifts each letter in a string by a given number.


def shift_letters(message: str, shift: int) -> str:
    """Shifts each letter in the message by the given shift value."""
    shifted_message = []  # List to store the shifted characters

    for char in message:
        if char.isalpha():  # Check if the character is a letter
            # Shift the letter by the shift value
            shifted_char = chr(ord(char) + shift)
            shifted_message.append(shifted_char)
        else:
            # If not a letter, add the character unchanged
            shifted_message.append(char)

    return "".join(shifted_message)  # Join the list into a string and return it


# Get user input
user_message = input("Enter a message to shift: ")
shift_value = int(input("Enter the shift value: "))

# Call the function and print the result
print(f"Shifted message: {shift_letters(user_message, shift_value)}")


# TASK: High Score Tracker
def update_highscores(scores: list, new_score: int) -> list:
    scores.append(new_score)
    scores.sort(reverse=True)
    return score[:5]


# Define a function that takes a list of scores and a new score
# Append the new score to the list
high_scores = []
# Sort the list in descending order
while True:
    new_score = int(input("Enter new score (to stop -1): "))
    if new_score == -1:
        break
    high_scores = update_highscores(high_scores, new_score)
    print(f"Updated score: {high_scores}")
# Keep only the top 5 scores

# Return the updated list

# Start with an empty high scores list

# Use a loop to let the user enter scores until they type -1

# Call the function with each new score and display the updated top 5 scores


# TASK: Grocery List Manager
def add_item(grocery_list: list, item: str) -> list:
    grocery_list.append(item)
    return grocery_list


# Define a function to add an item to the list
def remove_item(grocery_list: list, item: str) -> list:
    if item in grocery_list:
        grocery_list.remove(item)
    else:
        print(f"{item} is not in your list")
    return grocery_list


# Append the item to the list and return it

# Define a function to remove an item from the list


# If the item exists, remove it
def view_list(grocery_list: list) -> None:
    """Displays the current grocery list."""
    if grocery_list:
        print("\nYour Grocery List:")
        for index, item in enumerate(grocery_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your grocery list is empty.")


# If not, display a message saying the item is not in the list
grocery_list = []
# Define a function to display the grocery list

# If the list is not empty, print all the items with numbers
while True:
    print("\nOptions: (1) Add item (2) Remove item (3) View list (4) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter an item to add: ")
        grocery_list = add_item(grocery_list, item)
    elif choice == "2":
        item = input("Enter an item to remove: ")
        grocery_list = remove_item(grocery_list, item)
    elif choice == "3":
        view_list(grocery_list)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
# If the list is empty, display message

# Start with an empty grocery list

# Use a loop to let the user choose an action:
# (1) Add an item
# (2) Remove an item
# (3) View the list
# (4) Exit the program
# Call the corresponding function based on user input

# Continue looping until the user chooses to exit
