def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) -1

    while left <= right:

        middle = (right + left) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            # toss out the left side of the array 
            right = middle - 1 

        else:
            left = middle + 1
            
    return -1  # not found


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr1, 8))