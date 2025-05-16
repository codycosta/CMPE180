'''
Author:     Cody Costa
Date:       5/13/2025

'''

import math

def isPrime(num: int) -> bool:
    if num <= 0:
        print('Negative numbers are not prime nor composite, enter positive integers only')
        return
    elif type(num) != int:
        print('isPrime argument must be a positive integer')
        return
    
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    else:
        return True
    

# test cases
print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(5))

print(isPrime(0))
print(isPrime(-2))
print(isPrime(3.14))