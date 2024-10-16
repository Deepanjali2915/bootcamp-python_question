a = int(input())
b = int(input())

# i = 1
# while i<=a :
#     if(a % i == 0 and b % i == 0):
#         val = i
#     i = i + 1
    
# print(a, b, val)




i=2
z=1
while i<=a and i<=b:
    if(a % i == 0 and b % i == 0):
        a=a//i 
        b=b//i
        z*=i
    else:    
        i+=1 
print(z)        