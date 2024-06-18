'''19. Write a python program that removes all punctuation from a given string.'''
import string 
my_string = "Hello! How are you? I'm doing well, thanks." 

new_string = "" 
for char in my_string: 
    if char not in string.punctuation: 
        new_string += char 
print(new_string)
