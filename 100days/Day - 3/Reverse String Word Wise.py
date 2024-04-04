# TWo pointer approach

def reverseStringWordWise(string):

    wordList = string.split()
    i = 0
    j = len(wordList) - 1
    

    while i < j:

        wordList[i], wordList[j] = wordList[j], wordList[i]

        i+=1
        j-=1
    
    reversedString = ""
    
    for i in wordList:
        reversedString += i + " "
    
    return reversedString















    


string = input()
ans = reverseStringWordWise(string)
print(ans)
        
