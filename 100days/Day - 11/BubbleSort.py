# swap elements pull the largest to last in forst iteration 

# Time complexity - O(N^2)

def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n):
        for j in range(1, n - i):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]