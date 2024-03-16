def stockSpan(arr):
    countArray = []
    for i in range(len(arr)):
        count = 1
        for j in range(i):
            if(arr[i] >arr[j]):
                count+=1
            else:
                count = 1

        countArray.append(count)
    return countArray

# [1, 1, 1, 2, 1, 4, 6]
arr = [8, 60, 70, 80, 100, 90, 75, 80, 120]

print(stockSpan(arr))

