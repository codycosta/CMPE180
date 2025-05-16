'''
Author:     Cody Costa
Date:       5/13/2025

'''

collection = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_reversed_collection = []

for index in range(len(collection)):
    item = collection.pop()
    _reversed_collection.append(item)

print(_reversed_collection)