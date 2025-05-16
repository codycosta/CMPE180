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

TODO: delete(data) - Remove the first node containing the given data.

TODO: display_forward() - Print all node data from head to tail.

TODO: display_backward() - Print all node data from tail to head.

Bonus (optional)

Implement the following additional features:

TODO: insert_after(target_data, new_data) - Insert a new node with new_data after the node with target_data.

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

    def display_list(self):

        ''' displays the contents of the linked list '''

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


    def display_forward(self):
        ...

    def display_backward(self):
        ...

    def insert_after(self, data):
        ...

    def reverse(self):
        ...



''' testing code '''

mylist = Doubly_Linked_List()           # empty list []
mylist.append(4)
mylist.display_list()                   # [4]

mylist.append(5)
mylist.display_list()                   # [4, 5]

mylist.prepend(3)
mylist.display_list()                   # [3, 4, 5]

mylist.prepend(2)
mylist.display_list()                   # [2, 3, 4, 5]

mylist.prepend(4)
mylist.display_list()                   # [4, 2, 3, 4, 5]

mylist.delete(4)
mylist.display_list()                   # [2, 3, 4, 5]

mylist.delete(4)
mylist.display_list()                   # [2, 3, 5]