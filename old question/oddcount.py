# t=int(input())
# for _ in range(t):
#     n=list(map(int,input().split()))
#     i=0
#     count=0
#     while i<t:
#         if n[i]%2!=0:
#             count+=1
#         i+=1
#     if count>=1:
#         print(count)
#     else:
#         print("no odd no.")                
n,s,k=map(int,input().split())
p,q=list(map(int,input().split()))
i=0
while i<n:
    print(p[i]+q[i])
    i+=1
    