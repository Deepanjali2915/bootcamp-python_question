n = int(input())
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    x = b
    y = a + b
    a=x 
    b=y
    count += 1
