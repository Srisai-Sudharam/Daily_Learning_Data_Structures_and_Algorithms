# my first try using two pointers i, j not that for last character j is already out of boud so I did length - i

# def encode(message):
    
#     result = ""
#     i = 0
#     j = 1
#     length = len(message)

#     while j < length:
#         if message[i] != message[j]:
#             result += message[i] + str(j-i)
#             i = j
#         j+=1
#     result += message[i] + str(length  -i)

    
#     return result

# another approach using a counter to count frequency of chars


def encode(message):
    n = len(message)
    i = 0
    result = []
    while i < n:
        currentChar = message[i]
        charFreq = 1
        while i+1 < n and message[i+1] == currentChar:
            charFreq +=1
            i += 1
        result.append(currentChar)
        result.append(str(charFreq))
        i+=1
    
    encodedString = "".join(result)

    return encodedString
        




