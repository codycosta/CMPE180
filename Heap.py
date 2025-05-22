'''
Author: Cody Costa
Date:   5/22/2025

'''

# Prompt
'''
Objectives
Understand how a heap data structure works
Implement a heap data structure from scratch (not using the builtin classes in Python):

Implement a class MinHeap with the following methods:

insert(val)
extract_min()
display() (to print the internal list representation)

Internal helper methods should include:

_sift_up(index)
_sift_down(index)

Do not use the built-in heapq module or any external libraries for heap functionality.

Write a main() block that:

Inserts a predefined list of integers.
Displays the heap after each insertion.
Extracts elements one-by-one while displaying the heap at each step.
'''

class MinHeap:
    def __init__(self):
        self.root = []

    def _sift_up(self, index):
        ''' moves item toward the root of the MinHeap '''

        if index == 0:
            raise IndexError('can\'t sift up the 0th index')
            
        elif index > len(self.root):
            raise IndexError('heap index out of range')
            
        else:
            self.root[index], self.root[index - 1] = self.root[index - 1], self.root[index]


    def _sift_down(self, index):
        ''' moves item away from the root of the MinHeap '''

        if index == -1 or index == len(self.root) - 1:
            raise IndexError('can\'t sift down the last index')
            
        elif index > len(self.root):
            raise IndexError('heap index out of range')
            
        else:
            self.root[index], self.root[index + 1] = self.root[index + 1], self.root[index]


    def insert(self, value):
        ''' inserts value(s) into the heap'''

        # if multiple entries in one var
        if type(value) in [list, tuple]:
            for item in value:
                self.root.append(item)
        
        # if a single entry
        else:
            self.root.append(value)

        # sort to maintain min heap rules
        idx = 0
        while self.root != sorted(self.root):

            if idx != 0 and self.root[idx] < self.root[idx - 1]:
                self._sift_up(idx)
            elif idx != len(self.root) - 1 and self.root[idx] > self.root[idx + 1]:
                self._sift_down(idx)

            idx += 1

            if idx >= len(self.root):
                idx = 0

    
    def extract_min(self):
        ''' return the smallest value in the heap '''

        return self.root.pop(0)
    

    def display(self):
        ''' print out the current heap '''

        print(self.root)

    

def main():

    mylist = MinHeap()
    print('inserting values into heap\n')
    mylist.insert([3, 2, 1])
    mylist.display()
    mylist.insert([6, 4, 5, 1.4])
    mylist.display()

    print('\nremoving items from the heap\n')
    while mylist.root:
        mylist.extract_min()
        mylist.display()


main()
