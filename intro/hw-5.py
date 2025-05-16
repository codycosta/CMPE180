'''
Author:     Cody Costa
Date:       5/8/2025

'''

count = 1
while count <= 10:

    if count == 1:
        suffix = 'st'
    elif count == 2:
        suffix = 'nd'
    elif count == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    print(f'{count}{suffix} Hello')


    count += 1
