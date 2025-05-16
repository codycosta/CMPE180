'''
Author: Cody Costa
Date:   5/15/2025

'''

# Prompt
'''
You are to build a basic implementation of a Singly Linked List from scratch 
(i.e., no usage of Python lists or collections module for list storage). 
Your implementation should include a Node class and a SinglyLinkedList class that supports the following operations:

-------------------------------------------------------------------------------------

insert_at_head(data) - Insert a new node at the beginning (10 Marks)

insert_at_tail(data) - Insert a new node at the end (10 Marks)

insert_at_position(position, data) - Insert at a specific 0-based position (handle out-of-bounds) (10 Marks)

TODO: delete_node_by_value(value) - Delete the first node with the given value (10 Marks)

TODO: search(value) - Return the index of the node with the value, or -1 if not found (10 Marks)

TODO: display() - Print all elements in the list (5 Marks)

length() - Return the number of nodes in the list (5 Marks)

TODO: reverse() - Reverse the list in-place (10 Marks)

Provide at least five test cases demonstrating the functionality of your linked list, including:

Insertions at head and tail

Deletion

Reversal

Edge cases (e.g., deleting non-existent values, inserting at out-of-range positions)
'''



class Node:
    def __init__(self, data):
        self.data = data        # data for this node
        self.next = None        # pointer to next node in list



class Sinlgy_Linked_List:
    def __init__(self):
        self.head = None    # init list pointer


    def length(self):

        # if empty list
        if self.head == None:
            return 0
        
        # else min length is 1
        list_length = 1
        current_node = self.head

        # traverse through nodes in list incrementing length for each
        while current_node.next:
            list_length += 1
            current_node = current_node.next

        return list_length


    def insert_at_head(self, data):

        ''' inserts a value at the front of the linked list '''

        # data to insert
        new_node = Node(data)      

        # point new node to current head of list such that: linked_list.head && new_node --> rest of list
        new_node.next = self.head   

        # update head of list pointer to new_node as first item
        self.head = new_node        


    def insert_at_tail(self, data):

        ''' inserts a value at the end of the linked list '''

        # data to insert
        new_node = Node(data)           

        # if empty list
        if self.head == None:           
            self.head = new_node
            return
        
        # get current pointer position
        current_node = self.head        

        # move through list until pointer reaches no next element
        while current_node.next:        
            current_node = current_node.next

        # set pointer next to new data
        current_node.next = new_node    

    
    def insert_at_position(self, position, data):
        
        ''' inserts a new value at the specified position in the list '''

        # catch error case first
        if position > self.length() or position < 0:
            raise IndexError('insertion position is outside of list length, segmentation fault :(')
        
        # head / tail insert conditions
        if position == 0:
            self.insert_at_head(data)

        if position == self.length():
            self.insert_at_tail(data)

        
        # insert new data in middle of list
        new_node = Node(data)
        
        # navigate to target position (indexed from 0)
        current_node = self.head
        for _ in range(position - 1):
            current_node = current_node.next

        # point new_node.next to current_node.next
        new_node.next = current_node.next

        # point current_node.next to new_node
        current_node.next = new_node
        



''' testing code down here '''

mylist = Sinlgy_Linked_List()
# print(mylist.length())

mylist.insert_at_head(5)
# print(mylist.head.data, mylist.head.next)
# print(mylist.length())

mylist.insert_at_head(4)
# print(mylist.head.data)

mylist.insert_at_position(1, 3)

current = mylist.head
while current.next:
    print(current.data)
    current = current.next

print(current.data)