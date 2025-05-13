'''
Author:     Cody Costa
Date:       5/13/2025

'''

def Factorial(num: int):
    if num == 0:
        return 1
    result = 1
    for val in range(1, num + 1):
        result *= val
    return result

def Recursive_Factorial(num: int):
    if num == 0:
        return 1
    
    return num * Recursive_Factorial(num - 1)
    


print(Factorial(4))
print(Recursive_Factorial(4))

print(Factorial(0))
print(Recursive_Factorial(0))

print(Factorial(7))
print(Recursive_Factorial(7))
