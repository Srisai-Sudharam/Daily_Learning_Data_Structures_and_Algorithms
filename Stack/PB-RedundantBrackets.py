
from sys import stdin

def checkRedundantBrackets(expression) :
	stack = []
	# Your code goes here
	for char in expression:
		if char == ')':
			count = 0
			while(stack[-1] != '('):
				stack.pop()
				count+=1
			stack.pop()
			
			if(count < 2):
				return True
		else:
			stack.append(char)
	return False


expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
