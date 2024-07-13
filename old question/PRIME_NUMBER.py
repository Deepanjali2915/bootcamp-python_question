import math
def is_prime(n):
    if n <= 1:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True
 
n=int(input())
i=0
j=2
while i<n:
  count=0
  k=2
  while k<=j:
    if j%k==0:
      count+=1
    k+=1
  if count==1:
    print(j,end=" ")
    i+=1 
  j+=1  
          