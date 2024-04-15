n = int(input())
primes = []
num = 2

while len(primes) < n:
    is_prime = 1
    i = 2

    while i * i <= num:
        if num % i == 0:
            is_prime =0
            break
        i += 1

    if is_prime:
        primes = primes + [num]

    num += 1

print(f"The first {n} prime numbers are: {primes}")



