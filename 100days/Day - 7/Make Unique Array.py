def minElementsToRemove(arr):
    hash = {}
    count = 0
    for i in arr:
        if hash.get(i):
            count += 1
        else:
            hash[i] = True
    return count