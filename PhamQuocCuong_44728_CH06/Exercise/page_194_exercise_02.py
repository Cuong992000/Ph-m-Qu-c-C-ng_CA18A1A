"""
Author: Phạm Quốc Cường
Date: 21/10/2021
Problem:
    What is the scope of a variable? Give an example.
Solution:
    The scope of the module variables replacements and changePerson includes the entire module below the point where the variables are introduced. This includes the code nested in
    the body of the function changePerson. The scope of these variables also includes the nested bodies of other function definitions that occur earlier. This allows these variables
    to be referenced by any functions, regardless of where they are defined in the module. For example, the reply function, which calls changePerson, might be defined before changePerson
    in the doctor module.
"""