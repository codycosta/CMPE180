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

        # data to include
        new_node = Node(data)

        # check for empty tree
        if self.root == None:
            self.root = new_node
            return

        # init root pointer
        # root_val = self.root.value
        current = self.root

        while True:
            # check if value already exists in tree
            if data == current.value:
                print(f'{data} already exists in tree')
                return
            
            # look at right side
            if data > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return

            # look at left side
            elif data < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return

    # TODO
    def delete(self, data):
        ''' removes an item from the tree and restructures the tree '''
        
        if self.root == None:
            print('No tree elements, can\'t remove what isn\'t there')
            return
        
        # init root pointer
        current = self.root

        # check for current value
        if current.value == data:
            ...

        # will come back to this one

    
    def print_tree(self):
        ''' prints the tree with structured graphics '''

        if self.root == None:
            print('no tree to display')
            return
        
        tree = []

        def print_node(node, row=0):
            ''' prints the node + children '''

            # row += 1

            children = (node.left, node.right)
            if not children:
                return
            
            for child in children:
                if child == None:
                    continue
                print_node(child, row=row+1)

            # print(f'{node.value}')

            tree.append((row, node.value))

        
        current = self.root
        print_node(current)

        tree.sort()
        print(tree)

        cur_row = 0

        for (row, value) in tree:
            
            if row > cur_row:
                print('\n\n')

            cur_row = row    
            
            num_whitespace = ' ' * (60 // ( (2**row) + 1 ))
            print(f'{num_whitespace}{value}', end='')
            # print(f'{value}{num_whitespace}', end='')

            

        



def main():
    tree = Binary_Search_Tree()
    # root
    tree.insert(4)

    # children
    tree.insert(5)
    tree.insert(3)

    # grandchildren of 3
    tree.insert(2)
    tree.insert(3.5)

    # grandchildren of 5
    tree.insert(4.5)
    tree.insert(6)

    tree.print_tree()

main()