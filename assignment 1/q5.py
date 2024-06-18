'''5. Write a program that takes a string input from the user and writes it to a
text file.'''
user_input = input("Please enter a string: ")

# Specify the name of the file
file_name = "output.txt"

# Open the file in write mode and write the user input to the file
with open(file_name, 'w') as file:
    file.write(user_input)

print(f"The string has been written to {file_name}.")
