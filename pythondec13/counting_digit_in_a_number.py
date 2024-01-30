t=int(input())
total_sum = 0
count=0
while t > 0:
    total_sum = t % 10
    t //= 10
    count+=1 
print( count)
