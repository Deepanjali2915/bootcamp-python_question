a=[10,5,6,3,4,3,5,6]
min = a[0]
i = 1
while i < len(a):
    if a[i] < min:
        min = a[i]
    i += 1
print( a[i])
