import math
def is_prime(n):
    if n <= 1:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True
 
