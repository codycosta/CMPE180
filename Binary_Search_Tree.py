'''
Author: Cody Costa
Date:   5/18/2025

'''

# Prompt
'''
Implement a binary search tree in Python with the following functionalities:
Insert nodes via user input.
Perform in-order, pre-order, and post-order traversals.
Print the tree in a structured, tree-like format, clearly showing the hierarchy.

Define a class Node with:
Attributes: value, left, right.

Define a class BinarySearchTree with:
TODO: Method insert(value) - inserts value in the BST.
TODO: Method delete(value) - delete the value and restructure the tree.
TODO: Method in_order_traversal(node) - returns values in in-order.
TODO: Method pre_order_traversal(node) - returns values in pre-order.
TODO: Method post_order_traversal(node) - returns values in post-order.
TODO: Method print_tree() - prints the tree in a visually structured way.

Accept user input (comma-separated integers) and insert them into the tree.

After construction:
Print the tree using print_tree().
Print the three traversals.
Delete a node or two and reprint the tree using print_tree().
'''

class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None



class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    
    def insert(self, data):
        ''' inserts a given value into the tree '''

        new_node = Node(data)

        if self.root == None:
            self.root = new_node

        current = self.root

        while True:
            if data > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break

            elif data < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break

        

                

            

    
    def delete(self, data):
        ...


    