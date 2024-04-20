from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getGroupedAnagrams(inputStr):
        mp = {}
        ans = []

        for s in inputStr:
            sorted_str = ''.join(sorted(s))
            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
            else:
                mp[sorted_str] = len(ans)
                ans.append([s])
                
        return ans
    


def takeInput():

    n = stdin.readline().strip()
    inputStr = list(stdin.readline().strip().split(" "))

    return inputStr, n


def printAnswer(groupedAnagram):
    for group in groupedAnagram:
        group.sort()

    groupedAnagram.sort()

    print('\n'.join(map(' '.join, groupedAnagram)))


T = int(stdin.readline().strip())
for i in range(T):
    inputStr, n = takeInput()
    groupedAnagram = getGroupedAnagrams(inputStr)
    printAnswer(groupedAnagram)
