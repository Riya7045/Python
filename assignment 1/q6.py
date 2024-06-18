'''6. Write a program that reads the content of a text file and prints it to the
console.'''
# Specify the name of the file to be read
file_name = "output.txt"

# Open the file in read mode and read the content
with open(file_name, 'r') as file:
    content = file.read()

# Print the content to the console
print(content)
