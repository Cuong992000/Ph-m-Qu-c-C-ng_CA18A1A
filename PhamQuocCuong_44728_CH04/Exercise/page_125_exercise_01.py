"""
Author: Phạm Quốc Cường
Date: 22/9/2021
Problem:
        Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file.
Solution:

"""
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)