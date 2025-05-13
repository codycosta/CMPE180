'''
Author:     Cody Costa
Date:       5/13/2025

'''

sample_text = 'I love my dogs Weenie and Snorlax'
print(f'{sample_text=}')
uniques = set(sample_text.lower())
instances = []

for idx, item in enumerate(uniques):
    instances.append(0)
    for char in sample_text.lower():
        if char == item:
            instances[idx] += 1

    print(f'text contains {instances[idx]} {item} \'s')
