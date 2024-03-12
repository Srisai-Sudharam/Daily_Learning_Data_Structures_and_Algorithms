# reference -- https://www.youtube.com/watch?v=5TQRrtl8KlQ


def reverseStack(s1, s2):
    if len(s1) == 1:
        return s1
    
    while(len(s1) > 1):
        ele = s1.pop()
        s2.append(ele)
    
    temp = s1.pop()

    while(len(s2) > 0):
        ele = s2.pop()
        s1.append(ele)
    
    reverseStack(s1, s2)
    s1.append(temp)
    
    







s1 = [1, 2, 3, 4]
s2 = []
reverseStack(s1, s2)

print(s1)