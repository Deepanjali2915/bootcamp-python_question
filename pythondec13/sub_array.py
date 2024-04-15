string = "abcdef"
subarrays = []

i = 0
while i < len(string):
    subarray = ""
    j = i
    while j < len(string):
        subarray += string[j]
        subarrays.append(subarray)
        j += 1
    i += 1

print(subarrays)
