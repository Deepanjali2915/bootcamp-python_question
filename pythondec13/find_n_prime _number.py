n=int(input())
i=0
j=2
while i<n:
    count=0
    k=2
    while k<=j:
        if j%k==0:
            count+=1
        k+=1
    if count==1:
        print(j,end=" ")
        i+=1
    j+=1          
        
   

# n = int(input())
# i = 0
# num = 2  # Start checking from 2, the first prime number

# while i < n:
#     count = 0
#     k = 2
    
#     while k <= num:
#         if num % k == 0:
#             count += 1
#         k += 1
        
#     if count == 1:
#         print(num, end=" ")
#         i += 1
    
#     num += 1
