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

def ScoreFinder(players, scores, find_player):
    players = ' '.join(players)
    players = str(players)
    players = players.lower()
    players = players.split()
    y = 0
    z = 0
    while y < len(players):
        if find_player == players[i]:
            score = scores[i]
            find_player = find_player.title()
            z = 1
            break
        elif find_player != players[i]:
            y += 1
    if y == 1:
        print('OUTPUT', find_player, 'got a score of', score)
    else:
        print('OUTPUT player not found')

def Union(list1, list2):
    list3 = []
    i = 0
    while i < len(list1):
        if list1[i] in list2:
            list3.append(list1[i])
            i += 1
        else:
            i += 1
    return list3


            

