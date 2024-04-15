S=[]
T=[]
N=int(input())
A=list(map(int,input().split()))
for i in range(N-1):
    s,t=map(int,input().split())
    # S=S+[s]
    # T=T+[t]
# print(S,T)
# i=0
# while i<len(A)-1:   
    A[i+1]=A[i+1]+(A[i]//s)*t
    # i+=1
    # 
    print(A[-1])
print(A[-1])



 
# 10
# 32 6 46 9 37 8 33 14 31 5
# 5 5
# 3 1
# 4 3
# 2 2
# 3 2
# 3 2
# 4 4
# 3 3
# 3 1
