"""
Author: Pham Quoc Cuong
Date: 25/8/2021
Problem:
        Write an algorithm that describes the second part of the process of making change
        (counting out the coins and bills).
Solution:
        Step-1: Take the total amount and take variables for quarter, dime, nickel and penny and initialize them to zero.
        Step-2: if total amount >= 25 divide it by 25 and add 1 to quarter. Repeat the process until it is false.
        Step 3: if total amount >= 10 divide it by 10 and add 1 to dime. . Repeat the process until it is false.
        Step 4: if total amount >= 5 divide it by 5 and add 1 to nickel. . Repeat the process until it is false.
        Step 5: Add total amount to penny.
        Step 6: Number of quarter, dime, nickel and penny are the required changes.
"""