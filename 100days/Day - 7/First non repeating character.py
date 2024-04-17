# #Brute Force O(N^2) O(1)
# def firstNonRepeatingCharacter(str):
#     for i in range(len(str)):
#         hasDuplicate = False
#         for j in range(len(str)):
#             if i == j:
#                 continue
#             if str[i] == str[j]:
#                 hasDuplicate = True
#                 break
#         if not hasDuplicate:
#             return str[i]
#     return str[0]
    

#O(N), O(N)
def firstNonRepeatingCharacter(str):
    hash = {}
    for char in str:
        if hash.get(char):
            hash[char]+=1
        else:
            hash[char]=1
    
    for char in str:
        if hash[char] == 1:
            return char
    return str[0]
    