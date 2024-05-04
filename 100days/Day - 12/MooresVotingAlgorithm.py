def findMajorityElement(arr, n):
	ele = -1
	count = 0
	for curr_ele in arr:
		if count == 0:
			ele = curr_ele
			count = 1
		if ele == curr_ele:
			count += 1
		else:
			count -= 1
	num = 0
	for i in arr:
		if i == ele:
			num+=1
	if num > n//2:
		return ele 
	return -1