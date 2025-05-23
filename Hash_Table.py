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
            hash_val = sum(ord(char) for char in key) % self.size
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
        
        index = self._hash(key)

        current = self.slots[index]
        while current:
            if current.key == key:
                return current.value
            
            current = current.next

        return None
        



    def delete(self, key):
        ...


    def display(self):
        ...