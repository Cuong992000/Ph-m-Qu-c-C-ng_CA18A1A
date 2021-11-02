"""
Author: Phạm Quốc Cường
Date: 8/9/2021
Problem:
        Assume that the variables x and y refer to strings. Write a code segment that prints these strings in alphabetical order.
        You should assume that they are not equal.
Solution:

"""
my_str = input("Nhập một chuỗi: ")
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
   print(word)