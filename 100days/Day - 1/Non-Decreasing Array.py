def isPossible(arr, n):
    changed = False
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        if changed:
            return False

        if  i == 0 or arr[i+1] >= arr[i-1]:
            arr[i] = arr[i+1]
        else:
            arr[i+1] = arr[i]
        
        changed = True
    
    return True
        