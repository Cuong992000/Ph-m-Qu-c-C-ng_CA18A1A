"""
Author: Phạm Quốc Cường
Date: 8/10/2021
Problem:
    Write a loop that accumulates the sum of the numbers in a list named data.
Solution:

"""
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))