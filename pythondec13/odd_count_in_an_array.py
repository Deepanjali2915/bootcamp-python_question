a=[4,7,9,10,13,17]
i=0
count=0
while i<len(a):
    if a[i]%2!=0:
        count+=1
    i+=1
print(count)        