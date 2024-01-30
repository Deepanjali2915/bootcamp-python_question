arr = [1, 2, 2, 4]
subarrays = []
count=0
# Using nested loops to find all subarrays
for start in range(len(arr)):
    for end in range(start + 1, len(arr) + 1):
        subarray = arr[start:end]
        subarrays.append(subarray)
        for i in subarrays:
            if i%2==0:
            
    
print(len(subarrays))

