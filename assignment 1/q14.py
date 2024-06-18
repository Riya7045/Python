'''14. Write a program that reads multiple lines of input from the user until they
enter an empty line, then prints all the lines.'''
lines = []

while True:
    line = input("Enter a line (press Enter to finish): ")
    if line:
        lines.append(line)
    else:
        break

print("Lines entered by the user:")
for line in lines:
    print(line)
