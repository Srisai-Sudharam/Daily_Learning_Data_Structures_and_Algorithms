def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    rotatedArray = [0]*n
    for i in range(n):
        rotatedArray[(n-k+i) % n] = arr[i]
    return rotatedArray
