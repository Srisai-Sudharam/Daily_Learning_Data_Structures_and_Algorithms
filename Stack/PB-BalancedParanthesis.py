from StackUsingLL import Stack

def isBalancedParanthesis(string):
    s = []        
    for char in string:
        if char in '({[':
            s.append(char)
        elif char == ')':
            if( not s or s[-1]!='('):
                return False
            s.pop()
        elif char == '}':
            if( not s or s[-1]!='{'):
                return False
            s.pop()
        elif char == ']':
            if( not s or s[-1]!='['):
                return False
            s.pop()
    if( not s):
        return True
    else: 
        return False



string = input()

print(isBalancedParanthesis(string))
