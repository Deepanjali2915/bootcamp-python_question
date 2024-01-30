a=[12,5,9,22]
i=0
min=0
while i<len(a):
    print(a[i]) 
    if a[i]<a[min]:
        print(a[i]) 
        min=swap
        swap=i
        a[i]=a[min]
    i+=1
#print(a[i])     
print(a[swap])     
print(a[min]) 
