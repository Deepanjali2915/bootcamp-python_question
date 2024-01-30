t=int(input())
total = 0
# count=0
while t > 0:
    total += t % 10
    t //= 10
    # count+=1 
print( total)
