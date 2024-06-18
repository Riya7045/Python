'''11. Write a python program that generates the first n numbers in the
Fibonacci sequence'''
n = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
