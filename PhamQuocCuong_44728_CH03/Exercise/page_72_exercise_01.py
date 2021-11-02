"""
Author: Phạm Quốc Cường
Date: 8/9/2021
Problem:
Assume that the variable amount refers to 24.325. Write the outputs of the following statements:
a. print("Your salary is $%0.2f" % amount)
b. print("The area is %0.1f" % amount)
c. print("%7f" % amount)
Solution:
a. Your salary is $24.32
b. The area is 24.3
c. 24.325000
"""
amount=24.325
print("Your salary is $%0.2f" % amount)
print("The area is %0.1f" % amount)
print("%7f" % amount)
