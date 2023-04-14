def BinarySearch (arr, search_key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == search_key:
            return mid

        elif arr[mid] < search_key:
            left = mid + 1

        else:
            right = mid - 1

    return -1
if (__name__=="__main__"):
    # print(BinarySearch( [4, 8, 15, 16, 23, 42], 15))
    # print(BinarySearch( [-131, -82, 0, 27, 42, 68, 179], 42))  
     print(BinarySearch ( [11, 22, 33, 44, 55, 66, 77], 90))
    
