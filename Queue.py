'''
Author: Cody Costa
Date:   5/16/2025

'''

# Prompt
'''
Implement a Queue Data Structure from Scratch in Python

Understand the FIFO (First-In-First-Out) principle.
Implement basic queue operations: enqueue, dequeue, peek, is_empty, size.
Build an intuitive and efficient class-based queue system.
Create a Queue class using a Python list.

------------------------------------------------------------------------------

Implement the following methods:

enqueue(item): Add item to the rear.
dequeue(): Remove and return the front item.
peek(): View the front item without removing it.
is_empty(): Return True if queue is empty.
size(): Return the number of elements.
display(): Print the contents from front to rear.

------------------------------------------------------------------------------

Main program

Create a way to queue up several items
Add new items to the queue
Peek the next in queue (the front of the queue)
Remove some items from the queue

* Print out the queue after each of these operations
'''


class Queue:
    def __init__(self):
        # using a list to store data
        self.head = []


    def enqueue(self, item):

        ''' add item to end of queue '''
        if type(item) in [list, tuple]:
            for x in item:
                self.head.append(x)

        else:
            self.head.append(item)

    
    def dequeue(self):

        ''' remove and return the first item in the queue '''

        item = self.head.pop(0)
        return item
    

    def peek(self):

        ''' view first item without removing it '''

        return self.head[0]
    

    def is_empty(self):

        ''' checks if queue is empty '''

        if not self.head: 
            return True 
        return False
    

    def size(self):

        ''' returns number of elements in the queue '''
        return len(self.head)
    

    def display(self):

        ''' prints items from front to end '''
        print(self.head)

        

def main():
    my_queue = Queue()
    my_queue.enqueue([1, 2, 3, 'banana', 3.14, 'Cody Costa', 71])
    my_queue.display()
    print()
    my_queue.enqueue((12, 24.1))
    my_queue.display()
    print()
    front = my_queue.peek()
    print(f'{front=}')
    my_queue.display()
    print()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.display()
    print()



if __name__ == '__main__':
    main()
