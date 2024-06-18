'''21. Write a python program that counts the occurrences of a specific element
in a list.'''
my_list = [1, 2, 3, 4, 5, 2, 3, 2]

element_to_count = input("enter the element")
occurrences = my_list.count(element_to_count)

print("The element", {element_to_count}," occurs" ,{occurrences}, "times in the list.")
