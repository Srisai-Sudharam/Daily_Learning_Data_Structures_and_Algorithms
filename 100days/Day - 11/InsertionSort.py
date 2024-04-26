from typing import List

def insertionSort(n: int, arr: List[int]) -> None:

    for i in range(1, len(arr)):
        j = i-1
        temp = arr[i]
        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp        