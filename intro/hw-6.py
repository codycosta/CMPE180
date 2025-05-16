'''
Author:     Cody Costa
Date:       5/8/2025

'''

limit = int(input('Enter upper limit of calculations:      '))
while limit not in range(33):
    limit = int(input('Please enter a value less than 32:       '))

print('\nexp\t\t2^exp')
print('-' * 20)

for x in range(limit + 1):
    print(f'{x}\t|\t{2**x}')
