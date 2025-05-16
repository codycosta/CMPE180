'''
Author:     Cody Costa
Date:       5/8/2025

'''

import math

lower = int(input('Enter lower limit:   '))
upper = int(input('Enter upper limit:   '))

primes = []

for num in range(lower, upper + 1):
    for j in range(2, int(math.sqrt(num)) + 1):

        if num % j == 0:
            break
    else:
        primes.append(num)

print(primes)
