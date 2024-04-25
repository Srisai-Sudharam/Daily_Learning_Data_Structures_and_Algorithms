#optimal approach
def isSubSequence(str1, str2):
    str1_length = len(str1)
    j = 0

    for char in str2:
        if j == str1_length:
            break
        if char == str1[j]:
            j += 1
    
    if j < str1_length:
        return False
    return True
    
