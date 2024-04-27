# Selection sort
#  In every iteration find the minimum element and bring it to begining
# outerloop track the beginning position at which min element should be swapped

def selectionSort(arr,n):
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    