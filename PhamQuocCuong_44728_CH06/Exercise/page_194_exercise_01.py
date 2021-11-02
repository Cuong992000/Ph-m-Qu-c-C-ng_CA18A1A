"""
Author: Phạm Quốc Cường
Date: 21/10/2021
Problem:
Where are module variables, parameters, and temporary variables introduced and initialized in a program?
Solution:
When the function f is called, it does not assign 10 to the module variable x; instead, it assigns 10 to a temporary variable x. In fact, once the temporary variable is introduced, the module variable is no longer visible within function f. In any case,
the module variable’s value remains unchanged by the call. There is a way to allow a function to modify a module variable
"""