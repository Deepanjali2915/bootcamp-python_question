# binary=input()
# i=len(binary)-1
# sum=0
# power=0
# while i>=0:
# 	if binary[i]=="1":
# 		sum+=2**power
# 	power+=1
# 	i-=1
# print(sum)	

# print(10101//10)



# bin=int(input())
# i=0
# dic=0
# while bin>0:
#     b=bin%10
#     dic=dic+(b*(2**i))
#     bin=bin//10
#     i+=1
# print(dic)    
    

# a=int(input())
# i=0
# u=0
# v=1
# while i<a:
#     print(u,end=" ")
#     x=v
#     y=u+v
#     u=x 
#     v=y
#     i+=1

# dic=int(input())
# bin=""
# while 0<dic:
#     bin=str(dic%2)+ bin
#     dic=dic//2
# print(bin)    
    


n=int(input())
k=int(input())
i=0
while i<k:
    print((n+(i*2)),end=" ")
    i+=1
    

















