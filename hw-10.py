'''
Author:     Cody Costa
Date:       5/13/2025

'''

sample_string = 'abc123_!+-_()*&'
length = 0
num_alpha_numeric = 0

for char in sample_string:
    length += 1
    if char.isalnum():
        num_alpha_numeric += 1

print(f'{length=}\t{num_alpha_numeric=}')
