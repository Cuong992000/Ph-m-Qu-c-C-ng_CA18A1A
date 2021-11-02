"""
Author: Phạm Quốc Cường
Date: 21/10/2021
Problem:

Solution:

"""

import os

QUIT = '8'
COMMANDS = ('1', '2', '3', '4', '5', '6,', '7', '8')
MENU =""""1 list the current directory
2   move up
3   move down
4   number of files in the disrectory
5   size of the disrectory in bytes
6   search for a file name
7   view the contents of a file
8   quit the rogram"""



def acceptCommand():
    while True:
        command = input("enter nuber: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command


def findFiles(target, param):
    pass


def runCommand(command):
    if command == '1':
        print("called listCurrentDir")
        listCurrentDir(os.getcwd())
    elif command =='2':
        print("called moveUp")
        moveUp()
    elif command =='3':
        print("called moveDown")
        moveDown(os.getcwd())
    elif command =='4':
        print("the total number of file is", \
              countFiles(os.getcwd()))
    elif command == '5':
        print("the total number of file is", \
              countFiles(os.getcwd()))
    elif command == '6':
        target = input("enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("string not fond")
        else:
            for f in fileList:
                print(f)
    elif command == '7':
        print("called mviewFile")
        viewFile(os.getcwd())



def viewFile(dirName):
    lyst = list(filter(os.path.isfile, os.listdir(dirName) ))
    if len(lyst) == 0:
        print("the are no file in this dis directory")
    else:
        while True:
            print("File in" + dirName + ":")
            for element in lyst: print(element)
            fileName = input("enter a file name from there name: ")
            if not fileName in lyst:
                print("sorry. there is an error in your file name")
            else:
                f = open(fileName, 'r')
                print(f.read())
                break


def listCurrentDir(dirName):
    lyst = os.listdir(dirName)
    for element in lyst:
        print(element)



def moveUp():
    os.chdir("...")
def moveDown(currentDir):
    newDir = input("enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
            os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("Error: no such name")



def countFiles(path):
    count = 0
    lyst= os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count



def countBytes(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getssize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count


def findFile(target, path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFile(target, os.getcwd()))
            os.chdir("..")
    return files

if __name__ =='__main__':
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("have a nice day!")
            break


