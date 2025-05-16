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

delete_node_by_value(value) - Delete the first node with the given value (10 Marks)

search(value) - Return the index of the node with the value, or -1 if not found (10 Marks)

display() - Print all elements in the list (5 Marks)

length() - Return the number of nodes in the list (5 Marks)

reverse() - Reverse the list in-place (10 Marks)

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



class Singly_Linked_List:
    def __init__(self):
        self.head = None    # init list pointer

    
    def display_list(self):

        ''' displays the contents of the linked list '''

        if self.head is None:
            print('List is empty, nothing to display')
            return

        current = self.head
        while current.next:
            print(f'{current.data}, ', end='')
            current = current.next
        print(current.data)


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
        

    def delete_by_value(self, data):
        
        ''' deletes the first node that has the given value '''

        # check for empty
        if self.head is None:
            print('List is already empty')
            return
        
        # if val to remove is in the first list slot
        if self.head.data == data:
            self.head = self.head.next
            return

        # start pointer at beginning
        current_node = self.head

        # loop through nodes to get to (hopefully target value)
        while current_node.next and current_node.next.data != data:

            # next node
            current_node = current_node.next

        # if at end of list
        if current_node.next is None:
            print(f'value {data} not found')
            return
        
        # update pointer to skip node with value to remove
        current_node.next = current_node.next.next
        return


    def search(self, value):

        ''' searches for a given value within the list, returns True/False '''

        # if first node has value
        if self.head.data == value:
            return True
        
        # init pointer
        current_node = self.head

        # loop through nodes, checking for value, break if found
        while current_node.next:
            if current_node.data == value:
                return True
            
            current_node = current_node.next

        # value not found
        return False
    

    def reverse_list(self):

        ''' reverses the linked list '''

        # idea to loop through current list and insert_at_head() into another list object

        # create new list object
        new_linked_list = Singly_Linked_List()

        # catch empty list case
        if self.head is None:
            print('list is empty, can\'t reverse')
            return

        # start pointer
        current_node = self.head

        # loop through nodes
        while current_node.next:

            # insert data at head of new list
            new_linked_list.insert_at_head(current_node.data)

            # increment pointer
            current_node = current_node.next
        
        # insert last value for case where Node.next == None
        new_linked_list.insert_at_head(current_node.data)

        return new_linked_list



''' testing code down here '''

mylist = Singly_Linked_List()       # empty list []

mylist.insert_at_head(5)            # [5]
mylist.display_list()

mylist.insert_at_head(4)            # [4, 5]
mylist.display_list()

mylist.insert_at_position(1, 3)     # [4, 3, 5]
mylist.display_list()

mylist.delete_by_value(4)           # [3, 5]
mylist.display_list()

mylist.insert_at_tail(7)            # [3, 5, 7]
mylist.display_list()

print(mylist.search(3))             # True
print(mylist.search(6))             # False

print(mylist.length())              # 3

mylist.insert_at_tail('end')        # [3, 5, 7, 'end']
mylist.display_list()
print(mylist.length())              # 4

print('-' * 30)

reversed_list = mylist.reverse_list()
reversed_list.display_list()        # ['end', 7, 5, 3]