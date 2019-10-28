import math
"""
def is_prime(num):
    if num <2: return False
    if num<4: return True
    max = math.ceil(math.sqrt(num))
    for x in range(2, max):
        if num%x == 0:
            return False

    return True

num = input("Enter a number to see if it is prime:")

print(is_prime(int(num)))
"""

#Sieve Of Eratosthenes (give all primes smaller than n

def sieve_eratosthenes(num):
    values = [True for x in range(num+1)]
    values[0] = False
    values[1] = False
    max = math.ceil(math.sqrt(num))
    for i in range(2, max):
        if values[i]:
            for i in range(i*i, num+1, i):
                values[i] = False

    return [i for i, v in enumerate(values) if v ]

num = input("Enter a number to find all primes smaller:")

print(sieve_eratosthenes(int(num)))