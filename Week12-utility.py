#Lauren Decker
#CSCI 102 - Section C
#Week 12 - Part A

def PrintOutput(input_string):
    print('OUTPUT', input_string)

def LoadFile(filename):
    with open(filename, 'r') as f:
        string = f.read().splitlines()
        mylist = list[string]
    return mylist

