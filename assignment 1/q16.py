'''16. Write a program in python that counts the frequency of each character in
a string.'''
input_string = input("enter a string:")
count = {}
for char in input_string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# Print character count
print("Character count:")
for char, value in count.items():
    print(f"{char}: {value} times")
