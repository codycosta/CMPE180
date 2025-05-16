'''
Author: Cody Costa
Date:   5/16/2025

'''

# Prompt
'''
You must implement two classes: Node and DoublyLinkedList.

1. Node Class
Attributes:

data: Holds the data.

prev: Reference to the previous node.

next: Reference to the next node.

2. DoublyLinkedList Class
Implement the following methods:

append(data) - Add a node with data to the end of the list.

prepend(data) - Add a node with data to the beginning of the list.

delete(data) - Remove the first node containing the given data.

display_forward() - Print all node data from head to tail.

display_backward() - Print all node data from tail to head.

--------------------------------------------------------------------------
Bonus (optional)

Implement the following additional features:

insert_after(target_data, new_data) - Insert a new node with new_data after the node with target_data.

TODO: reverse() - Reverse the linked list in-place.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



class Doubly_Linked_List:
    def __init__(self):
        self.head = None


    def display_forward(self):

        ''' displays the contents of the linked list from head to tail '''

        if self.head is None:
            print('List is empty, nothing to display')
            return

        current = self.head
        while current.next:
            print(f'{current.data} <--> ', end='')
            current = current.next
        print(current.data)


    def append(self, data):
        
        ''' inserts a value at the end of the list '''

        # new data node
        new_node = Node(data)

        # check for empty list first
        if self.head is None:
            self.head = new_node
            return
        
        # start pointer at front of list
        current = self.head

        # traverse to end of list
        while current.next:
            current = current.next

        # set new data
        current.next = new_node

        # mark previous node
        new_node.prev = current
        

    def prepend(self, data):
        
        ''' inserts a value at the front of the list '''

        # new data node
        new_node = Node(data)

        # check for empty list first
        if self.head is None:
            self.head = new_node
            return
        
        # start pointer
        current = self.head

        # traverse to beginning of list
        while current.prev:
            current = current.prev

        # set new data
        current.prev = new_node

        # mark next node
        new_node.next = current

        # define new start of list
        self.head = new_node


    def delete(self, data):
        
        ''' removes the first instance of the given value from the list '''

        # check for empty list first
        if self.head is None:
            print('list is empty')
            return
        
        # edge case for front of list
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        # move through list, looking for value to rm
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        # if at end of list
        if current.next is None:
            print(f'value {data} not found')
            return
        
        # skip node with value 
        link = current.next.next

        current.next = link
        link.prev = current


    def display_backward(self):
        
        ''' displays list contents from tail to head (reverse order) '''

        if self.head is None:
            print('List is empty, nothing to display')
            return
        
        # establish starting point at end of list
        current = self.head
        while current.next:
            current = current.next

        # loop backwards through list
        while current.prev:
            print(f'{current.data} <--> ', end='')
            current = current.prev
        print(current.data)

    
    ''' bonus functions '''

    def insert_after(self, data, value):
        
        ''' inserts the given value after the given data point in the list '''
        # reuse search func from Singly_Linked_List lol
        def search(data):

            ''' searches for a given value within the list, returns True/False '''

            # if first node has value
            if self.head.data == data:
                return True
            
            # init pointer
            current_node = self.head

            # loop through nodes, checking for value, break if found
            while current_node.next:
                if current_node.data == data:
                    return True
                
                current_node = current_node.next

            # value not found
            return False
        
        if not search(data):
            print(f'given value {data} not found in list, value {value} was not inserted')
            return
        
        new_node = Node(value)
        
        current = self.head

        while current.next and current.data != data:
            current = current.next

        # current.data should be the given {data} point now
        # take note of end link
        link = current.next

        # insert new value
        current.next = new_node
        new_node.next = link
        link.prev = new_node
        new_node.prev = current

        # current <--> new <--> link


    def reverse(self):
        ...



''' testing code '''

mylist = Doubly_Linked_List()           # empty list []
mylist.append(4)
mylist.display_forward()                # [4]

mylist.append(5)
mylist.display_forward()                # [4, 5]

mylist.prepend(3)
mylist.display_forward()                # [3, 4, 5]

mylist.prepend(2)
mylist.display_forward()                # [2, 3, 4, 5]

mylist.prepend(4)
mylist.display_forward()                # [4, 2, 3, 4, 5]

mylist.delete(4)
mylist.display_forward()                # [2, 3, 4, 5]

mylist.delete(4)
mylist.display_forward()                # [2, 3, 5]

mylist.display_backward()               # [5, 3, 2]

mylist.insert_after(3, 7)
mylist.display_forward()                # [2, 3, 7, 5]