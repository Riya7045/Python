'''27. Write a program in python that converts a string into a list of its characters.'''
def convert(string):
    li =list(string.split("-"))
    return li
str1 = input("enter the string:")
print(convert(str1))
