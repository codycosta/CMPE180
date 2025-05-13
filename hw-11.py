'''
Author:     Cody Costa
Date:       5/13/2025

'''

sample_string = input('Enter some string:   ')
search_char = input('Enter a character within the string to search for:     ')

instances_of_search_char = []

for idx, char in enumerate(sample_string):
    if char == search_char:
        instances_of_search_char.append(idx)

print(f'First occurrence = {instances_of_search_char[0]}\tLast occurrence = {instances_of_search_char[-1]}')
