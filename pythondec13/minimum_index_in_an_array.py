a=[10,5,6,3,4,1,5,6]
min=a[0]
mini=0
i = 0
while i < len(a):
    if a[i] < min:
        min = a[i]
        mini=i
    i += 1
print( mini)
