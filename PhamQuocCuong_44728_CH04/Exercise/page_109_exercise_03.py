"""
Author: Phạm Quốc Cường
Date: 22/9/2021
Problem:
        You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can contain any of the printable ASCII
        characters. Suggest an algorithm for cracking this code
Solution:

"""
def decoded(s):
    for i in range(1,95):
        string = ""
        for char in s:
            if(ord(char) + i > 126):
                charc = (ord(char) + i) - 94
                string =  string + chr(charc)
            else:
               charc = ord(char) + i
               string =  string + chr(charc)

        print(string)
decoded("T! x$r&'}r&z! %21j!'1~zxy&1\"r%%1TZedBEAB?")