# Driver code to test insertion sort
arr = [120, 11, 13, 25, 6]

# Traverse through 1 to len(arr)
for i in range(1, len(arr)):
    key = arr[i]
    
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

# Print the sorted array
for i in range(len(arr)):
    print(arr[i], end=" ")

