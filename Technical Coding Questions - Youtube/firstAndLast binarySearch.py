def firstEntry(arr, target):
    if target == arr[0]:
        return 0
    else:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid-1] < target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def lastEntry(arr, target):
    if target == arr[-1]:
        return len(arr)-1
    else:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid + 1] > target:
                return mid
            elif arr[mid] > target:
                return mid-1
            else:
                left = mid + 1
    return -1


arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
target = 5
# Want to immediately return [-1,-1] if target is not in arr
if target > arr[-1] or target < arr[0] or len(arr) == 0:
    print("[-1, -1]")
else:
    print("[", firstEntry(arr, target), ", ", lastEntry(arr, target), "]")
