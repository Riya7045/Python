'''15. Write a program that reads data from a CSV file and prints it to the
console.

import csv

# Specify the data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'London']
]

# Specify the filename
csv_filename = "data.csv"

# Write data to the CSV file
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file 'data.csv' created successfully.")
'''

import csv
csv_filename = "data.csv"

try:
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File 'data.csv' not found.")

