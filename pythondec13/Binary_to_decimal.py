# n=(input())
# d=0
# b=len(n)
# i=0
# while i<b:
#     a=int(n[i])
#     d=(d*2)+a 
#     i+=1
# print(d)    


# a=[1,1,0,1,1]
# i=0
# sum=0
# sum1=0
# number=len(a)-1
# while i<len(a):
#     b=a[number]
#     sum=(2**i*b)
#     number-=1
#     i+=1
#     sum1+=sum
# print(sum1)  


# n=int(input())
# for _ in range(n):
#     t=int(input())
a=str(input())
i=0
sum=0
sum1=0
number=len(a)-1
while i<len(a):
    b=a[number]
    sum=(2**i*b)
    number-=1
    i+=1
    sum1+=sum
print(sum1)  
