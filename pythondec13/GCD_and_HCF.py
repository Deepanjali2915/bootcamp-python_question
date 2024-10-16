# m,n=map(int,input().split())
# if m>n:
#     max=m 
#     min=n
# else:
#     max=n
#     min=m
# number=max
# if number%min!=0:
#     number+=max
#     print(number)            
# else:
#     print(m*n)


a = int(input())
b = int(input())
i=2
z=1
while i<=a and i<=b:
    if(a % i == 0 and b % i == 0):
        a=a//i 
        b=b//i
        z*=i
    else:    
        i+=1         
print(z*a*b)