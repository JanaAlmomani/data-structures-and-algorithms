def insertShiftArray(arr, val):
    mid = len(arr) // 2  
    n=len(arr)
    arr.append(" ")  
    for i in range(len(arr)-1, mid, -1):
        arr[i] = arr[i-1] 
    if(n%2==0):
            arr[mid] = val
    else:
            arr[mid+1] = val
    return arr

if (__name__=="__main__"):
    
    print(insertShiftArray( [2,4,6,-8],5))  
    # [2,4,5,6,-8]
    print(insertShiftArray( [42,8,15,23,42], 16))  
    #  [42,8,15,16,23,42]

