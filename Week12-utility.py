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
def FindWordCount(list1, string1):
    i = 0
    list1 = (''.join(list1)).split()
    for x in list1:
        if x == string1:
            i += 1
    return i

