'''
	Time Complexity: O(N)
	Space Complexity: O(1)

	Where N is the length of the string.
'''

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)


def nextLargestPalindrome(s, length):
    carry = 1
    lst = list(s)
    # Loop to add 1 to the number.
    for i in range(length - 1, -1, -1):
        digit = int(lst[i])
        if digit + carry <= 9:
            lst[i] = chr(digit + carry + 48)
            carry = 0

        else:
            temp = (int(lst[i]) + carry) % 10
            lst[i] = chr(temp + 48)
            carry = 1

    s = ''.join(lst)
    if carry:
        s = "1" + s

    i, j = 0, len(s) - 1
    pos = -1
    conditionViolated = False
    s = list(s)
    while i <= j:
        if s[i] < s[j]:
            s[j] = s[i]
            pos = i
            conditionViolated = True

        elif s[i] > s[j]:
            s[j] = s[i]
            conditionViolated = False

        elif conditionViolated and s[i] != '9':
            pos = i

        i += 1
        j -= 1
    # Checking if the condition is violated or not.
    # Finding the smallest palindrome strictly greater than the input number.
    if conditionViolated:
        s[pos] = chr(int(s[pos]) + 1 + 48)
        s[len(s) - 1 - pos] = s[pos]
        for i in range(pos + 1, (len(s) - 1) // 2 + 1):
            s[len(s) - 1 - i] = s[i] = '0'

    return ''.join(s)





























# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    S = stdin.readline().strip()
    return N, S


tc = int(input())
while tc > 0:
    N, S = takeInput()
    S = nextLargestPalindrome(S, N)
    stdout.write(S + "\n")
    tc -= 1
