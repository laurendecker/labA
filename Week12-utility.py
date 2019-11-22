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

def UpdateString(str1, str2, x):
    str1 = list(str1)
    str1[x] = str2
    str1 = ''.join(str1)
    updatedstring = str(str1)
    print('OUTPUT', updatedstring)
