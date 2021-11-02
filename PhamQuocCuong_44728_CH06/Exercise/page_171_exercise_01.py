"""
Author: Phạm Quốc Cường
Date: 21/10/2021
Problem:
    Anne complains that defining functions to use in her programs is a lot of extra work. She says she can finish her programs much more quickly if she
    just writes them using the basic operators and control statements. State three reasons why her view is shortsighted.
Solution:
Functions in Python
• Functions are a group of logically related statements that are bundled together.
• A large program is complex to maintain and test. Hence it is divided into small pieces of code that are related
together which are known as functions.
• Functions take one or more inputs and return one ore no values as output.
• If a part of code is repeated more than one time in the code, then such parts of code are written as functions and
called continuously to reduce the redundancy of code.
• A function is executed in response to a function call and the control is returned to the functional call soon after the
execution of the function.
• A function can be called from any part of the program. Sometimes a function is called a part of other functions.
Example
Recursive functions are those in which the function is called itself in the function body
Reasons for Anne's Shortsighted view
1. Functions reduce redundancy
Redundancy is the presence of duplicate statements in the code.
• If the same fragment of code is being used in our program for more than one time then writing that repeated pa
of the code in the function reduces the redundancy.
The defined function can be called any number of times as per the requirement
2. Functions increase the readability of the code
. If a function is large and contains many lines of code then it is difficult for anyone to go through these lines of
code and understand them.
• If the code is divided into functions where each function is meant for a specified task the code becomes more
readable and convenient.
3. The function makes testing a part of the program easier
• If you have to test a particular part of a program during the construction of a huge project, then running the entire
program to test a particular part of code doesn't make sense.
• In such situations, if the part of the program to be tested is defined as a function then the function can be tested
apart which doesn't interfere with the remaining parts of the code.
4. Modification to the program becomes easier.
.
If you want to modify a particular part of code, then making such a task becomes easier if functions are used.
• If functions don't use the part of the program to which modifications should be made might have repeated
somewhere in the program which should be identified.

"""
from functools import reduce
reduce(max, [34, 21, 99, 67, 10])