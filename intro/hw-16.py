'''
Author:     Cody Costa
Date:       5/13/2025

'''

# define trivial function
def prAsterisk(num: int):
    # give function a counter attribute
    prAsterisk.counter += 1
    print('*' * num)

# set initial function counter to 0
prAsterisk.counter = 0

# call functions some number of times
for j in range(1, 8):
    prAsterisk(j)

# print count of how many times prAsterisk was called
print(prAsterisk.counter)