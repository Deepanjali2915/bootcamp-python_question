a=[5,4,4,7,6,3,2,4,6,8,6,3,6,8,6,]
i=0
count=1
store=[]
while i<len(a)-1:
    if a[i]<a[i+1]:
        count+=1
    else:
        #print(count)
        store.append(count)
        count=1
    i+=1    
print(count)        
j=0
max=0
while j<len(store):
    if store[j]>store[max]:
        max=j
    j+=1
print(store[max])
         

      

               
        
    #i+=1
#print(count)
#print(countt)
        
                    
