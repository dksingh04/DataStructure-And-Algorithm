def binarySearch(a, key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + ((high - low)//2)

        if a[mid] == key:
            return mid
        
        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

print(binarySearch([10, 27, 47, 59, 63, 75, 88, 99, 107, 120, 133, 140], 47))
print(binarySearch([10, 27, 47, 59, 63, 75, 88, 99, 107, 120, 133, 140], 64))
