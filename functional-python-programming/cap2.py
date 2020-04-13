import math

def numbers():
    for i in range(1024):
        print("=", i)
        yield i

def sum_to(n):
    sum = 0
    for i in numbers():
        if i == n: break
        sum += i
        print('sum = {}'.format(sum))
    return sum

print(sum_to(20))

# Tail-Call Optimization
isPrime = lambda x: not any(x % p for p in range(2, int(math.sqrt(x)) + 1))

def isprimer(n):
    def isprime(k, coprime):
        """Is k relatively prime to the value coprime?"""
        if k < coprime * coprime: return True
        if k % coprime == 0: return False
        return isprime(k, coprime + 2)
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime(n, 3)

print(isprimer(2))
print(isprimer(5))
print(isprimer(7))
print(isprimer(9))
