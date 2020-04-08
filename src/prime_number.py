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


# Sieve Of Eratosthenes (give all primes smaller than n

def sieve_eratosthenes ( num ):
    values = [True for x in range(num + 1)]
    values[0] = False
    values[1] = False
    max = math.ceil(math.sqrt(num))
    for i in range(2, max):
        if values[i]:
            for i in range(i * i, num + 1, i):
                values[i] = False

    return [i for i, v in enumerate(values) if v]


#num = input("Enter a number to find all primes smaller:")

print(sieve_eratosthenes(int(3000)))

start_num: int = 2
ending_num: int = 120
looping_list: list = [2, 3, 5, 7, 9]
result_list: list = [True] * ending_num

# Cross off numbers in the list which are not prime via process of elimination
for i in looping_list:
    for j in range(i * 2, ending_num, i):
        result_list[j] = False

# Display the prime numbers to the console
print('Prime numbers: ', end='')
for i in range(start_num, ending_num):
    if result_list[i]:
        print(str(i), end=', ')

print('...')
#
#
# def slowestKey ( keyTimes ):
#     stored = 0
#     max = 0
#     maxKey = ''
#     for i in range(len(keyTimes)):
#         letter = chr(keyTimes[i][0] + 97)
#         time = keyTimes[i][1] - stored
#         stored = keyTimes[i][1]
#         if (time > max):
#             max = time
#             maxKey = letter
#     return maxKey
#
# testKeyTimes= [[0,3],[20,5]]
#
# print(slowestKey(testKeyTimes))
#
