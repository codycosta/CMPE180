'''
Author: Cody Costa
Date:   5/22/2025

'''

# Prompt
'''
Objectives

Understand how hashing works.

Build a hash table from first principles.

Practice key-value data manipulation and collision handling.

Implement a class HashTable with the following features:

__init__(self, size): Initializes the hash table with the given size.

_hash(self, key): Implements a custom hash function based on string characters.

insert(self, key, value): Inserts or updates a key-value pair.

get(self, key): Retrieves the value for the given key.

delete(self, key): Deletes the key-value pair for the given key.

display(self): Displays the contents of the hash table with their respective indices.

Using your hash table:

Insert at least 10 key-value pairs, using fruit names as keys and arbitrary numbers as values.

Retrieve and print values for at least two keys.

Delete one key, then display the updated hash table.
'''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def _hash(self, key):
        ''' gives the key a unique index in the hash table '''

        # typical and basic hash function 
        if type(key) == str:
            hash_val = sum(ord(char.upper()) for char in key) % self.size
        else:
            hash_val = key % self.size

        return hash_val
        
        
    def insert(self, key, value):
        ''' inserts value into the hash table, or updates an existing entry '''

        # get index in table for new entry
        index = self._hash(key)

        #insert new value
        if self.slots[index] == None:
            self.slots[index] = Node(key, value)
            return

        # update existing key with new value
        else:
            current = self.slots[index]
            while current:

                # update value of matching key
                if current.key == key:
                    current.value = value
                    return
                
                # if at end of list of Nodes at this index
                if current.next == None:
                    break

                # iterate through Nodes at this index
                current = current.next

            # append new Node to list of Nodes at this index
            current.next = Node(key, value)

    
    def get(self, key):
        ''' retreives value for a given key '''
        
        # index based on hash function
        index = self._hash(key)

        # start iterator Node
        current = self.slots[index]

        # continue so long as another Node follows
        while current:

            # return match
            if current.key == key:
                return current.value
            
            # update pointer
            current = current.next

        # loop done, key not found in Node list at the hash index
        return None
        

    def delete(self, key):
        ''' removes the key-value pair for the given key '''
        
        # get index for given key
        index = self._hash(key)

        # check if key exists in table first
        if not self.get(key):
            print(f'{key} does not exist in table')
            return

        # find key-value pair for index in hash table
        current = self.slots[index]

        # skip first node in linked list
        if current.key == key:
            self.slots[index] = current.next
            return

        # loop to node that matches key
        while current.next and current.next.key != key:
            current = current.next

        # skip node with matching key
        current.next = current.next.next


    def display(self):
        ''' display contents of the hash table '''

        for idx, lst in enumerate(self.slots):

            if lst is None:
                print(f'Linked list for index {idx} is empty, nothing to display')
                continue
            
            current = lst
            index = self._hash(current.key)

            print(f'{index}:\t', end='')

            while current.next:
                print(f'({current.key}, {current.value}) --> ', end='')
                current = current.next
            print(f'({current.key}, {current.value})')



def main():
    import random

    ht = HashTable(20)
    # ht.display()

    fruits = ['apple', 'banana', 'strawberry', 'grape', 'orange', 'dragonfruit', 'pineapple', 'mango', 'blueberry', 'nectarine']
    vals = [random.randint(0, 50) for _ in range(10)]

    for idx, name in enumerate(fruits):
        ht.insert(name, vals[idx])

    print('\nInitial Build of Hash Table')
    ht.display()
    print('\n\n')

    # get values for 2 keys
    print('Retreive 2 values from table')
    print(f'Key: apple == {ht.get('apple')}\nKey: grape == {ht.get('grape')}')
    print('\n\n')

    # remove an element
    print('Modified Hash Table')
    ht.delete('pineapple')
    ht.display()
    print()



main()
