
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



a="11101"
i=len(a)
sum=0
while i>=0:
    if a[i]=="1":
        print(a[i],i)
        sum+=2**i
        print(sum) 
    i-=1
print(sum,"ss")        