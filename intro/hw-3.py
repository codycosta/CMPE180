'''
Author:     Cody Costa
Date:       5/8/2025

'''

year = int(input('Enter a year:     '))

# determine if leap year
if not year % 4 and ( year % 100 or not year % 400 ):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

