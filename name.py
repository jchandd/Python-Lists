# TASK: Write a function that shifts each letter in a string by a given number.
def shift_letter(message: str, shift: int) -> str:
# Define a function that takes a string and an integer shift value as parameters
shifted_message = []
# Create an empty list to store the shifted characters
for char in message 
    if char.isalpha():
        shifted_char = chr(ord(char) + shift)
        shifted_message.append(shifted_char)
    else
        shifted_message.append(char)
# Loop through each character in the string:
return ''.join(shifted_message)
#    If the character is a letter (A-Z or a-z):
#        Shift the letter by adding the shift value to its ASCII code (use the ord function)
#        Convert the new ASCII code back to a character (use the chr function)
#        Add the shifted character to the list
#    If the character is not a letter:
#        Add the character unchanged to the list

# After the loop, join the list into a string and return it

# Get user input for the message and shift value
user_message = input("ENter a message to code: ")
shift_value = int(input("Enter the shift value: "))
# Call the function with the inputs and display the result
print(f"Shifted message: {shift_letters(user_message, shift_value)}")