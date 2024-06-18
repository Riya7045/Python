'''22. Write a python program that returns the minimum and maximum values
in a list of numbers.'''
input_string = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in input_string.split()]
min_value = min(numbers)
max_value = max(numbers)

print("Minimum value:", min_value)
print("Maximum value:", max_value)
