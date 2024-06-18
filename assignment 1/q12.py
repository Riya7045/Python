'''12. Write a python program that calculates the sum of the digits of a given
number'''
n = int(input("enter the number"))
sumofdigits = 0
while number >0:
    digit = n%10 #extract the last digit
    sumofdigit+=digit #add the digit to the sum
    n //= 10 #remove the last digit
print("the sum of digits is :", sumofdigit)
