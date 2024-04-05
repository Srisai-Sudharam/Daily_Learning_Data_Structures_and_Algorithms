## There are only two possible strings that can be created


# Approach - 1
# T = O(N)
# space = O(N)

# def makeBeautiful(str):
# 	# Write your code here
# 	length = len(str)	
# 	possibilityOne = "10" * (length // 2)
# 	possibilityTwo = "01" * (length // 2)

# 	if length % 2 != 0:
# 		possibilityOne += "1"
# 		possibilityTwo += "0"
	
# 	changeToMakeOne = 0
# 	changeToMakeTwo = 0
# 	for i in range(length):
# 		if str[i] != possibilityOne[i]:
# 			changeToMakeOne += 1
# 		if str[i] != possibilityTwo[i]:
# 			changeToMakeTwo += 1

# 	return min(changeToMakeOne, changeToMakeTwo) 


# Approach - 2
# Time = O(N)
# Space = O(1)


def makeBeautiful(str):
    t1 = 0 #counts wrt string starting with 0 
    t2 = 0 #counts wrt string starting with 1
    s1 = "0" #string starting with 0
    s2 = "1" #string starting with 1

    for char in str:
        if char == "1":
            if s1 =="0":
                t1 += 1
            else:
                t2 += 1
        else:
            if s1 == "1":
                t1 += 1
            else:
                t2 += 1

        # inverting  s1 and s2
        if s1 == "0":
            s1 = "1"
        else:
            s1 = "0"

        if s2 == "0":
            s2 = "1"
        else:
            s2 = "0"
    return min(t1, t2)


string = input()
print(makeBeautiful(string))