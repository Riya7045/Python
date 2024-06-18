'''25. Write a program that copies the contents of one text file to another.'''
source_file = "output.txt"
destination_file = "source.txt"

# Open the source file in read mode and destination file in write mode


with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    # Read from source and write to destination
    dest.write(src.read())

print("Contents of",{source_file}," have been copied to",{destination_file})
