
# binary = input()
# decimal = 0
# power = len(binary) - 1
# index = 0

# while index < len(binary):
#     if binary[index] == '1':
#         decimal += 2 ** power
#     power -= 1
#     index += 1

# print(decimal)



# a="11101"
# i=len(a)
# sum=0
# while i>=0:
#     if a[i]=="1":
#         print(a[i],i)
#         sum+=2**i
#         print(sum) 
#     i-=1
# print(sum,"ss")        



# bin=int(input())
# i=0
# dic=0
# while bin>0:
#     b=bin%10
#     dic=dic+(b*(2**i))
#     bin=bin//10
#     i+=1
# print(dic)    




a = int(input())
i = 0
c=0
while a > 0:
    b = a%10
    c = c + (b*(2**i))
    a = a//10 
    i += 1 
print(c)    




































