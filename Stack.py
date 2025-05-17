'''
Author: Cody Costa
Date:   5/16/2025

'''

# Prompt
'''
Objectives

Implement a stack data structure from scratch in Python.

Understand core stack operations and apply them in simple problem-solving scenarios.

Implement a class Stack with the following methods:

__init__(self): Initialize an empty stack.

push(self, item): Add an item to the top of the stack.

pop(self): Remove and return the top item from the stack. Handle underflow.

peek(self): Return the top item without removing it.

is_empty(self): Return True if the stack is empty, otherwise False.

size(self): Return the number of elements in the stack.

display(self): Print the stack from top to bottom.

Use print statements where necessary to visualize each operation.

--------------------------------------------------------------------------
main program

Solve the following problems using your Stack class:

Balanced Parentheses Checker
Write a function that checks if a string of brackets (e.g., "(()[]){}") is balanced.

Reverse a String Using a Stack
Write a function that uses a stack to reverse a given string.

Evaluate Postfix Expression
TODO: Implement a postfix (Reverse Polish Notation) expression evaluator, e.g., "3 4 + 2 * 7 /".

Undo Operation Simulation
TODO: Simulate an undo feature using a stack where actions are pushed and undone via pop.
'''


class Stack:
    def __init__(self):
        # use list object as our stack storage
        # left == bottom, right == top of stack
        self.head = []


    def push(self, item):
        ''' push item to top of stack (end of list)'''
        
        # case to push several items to stack if in the form of list, tuple type
        if type(item) in [list, tuple]:
            for x in item:
                self.head.append(x)
        
        # push single item
        else:
            self.head.append(item)


    def pop(self):
        ''' remove top item from stack '''
        
        # catch empty stack case
        if not self.head:
            print('Stack is empty, nothing to pop')
            return
        
        # pop and return the top element
        top = self.head.pop()
        return top
        

    def peek(self):
        ''' take a look at the top element in the stack, without removal '''

        return self.head[-1]


    def is_empty(self):
        ''' check for empty stack '''

        if not self.head:
            return True
        
        return False


    def size(self):
        ''' return the length of the stack '''

        return len(self.head)


    def display(self):
        ''' display the stack '''
        
        print(self.head)



def reverse_string(text):
    ''' reverses a given string, returns new string object '''

    # fill Stack with characters in input string
    myStack = Stack()
    for char in text:
        myStack.push(char)
    
    # init new string to fill in reverse
    new_str = ''

    # fill new string by popping the stack until empty
    while not myStack.is_empty():
        char = myStack.pop()
        new_str += char

    return new_str


def parentheses_checker(text):
    ''' checks if a string of brackets is balanced (opened and closed properly) '''

    # check for even number of elements in input text
    if len(text) % 2:
        return False
    
    # push parenthetic state to new stack
    order_of_operations = Stack()

    for char in text:
        match char:

            case '(':
                order_of_operations.push('expecting close parentheses')
            case ')':
                if order_of_operations.peek() == 'expecting close parentheses':
                    order_of_operations.pop()
                else:
                    return False
                
            case '[':
                order_of_operations.push('expecting close bracket')
            case ']':
                if order_of_operations.peek() == 'expecting close bracket':
                    order_of_operations.pop()
                else:
                    return False
                
            case '{':
                order_of_operations.push('expecting close brace')
            case '}':
                if order_of_operations.peek() == 'expecting close brace':
                    order_of_operations.pop()
                else:
                    return False
                
    if order_of_operations.is_empty():
        return True
    
    return False




def main():
    # reverse string
    text = 'Cody Costa'
    text_rev = reverse_string(text)
    print(text, text_rev)

    # parentheses checker
    print(parentheses_checker(r'(()[]){}'))


if __name__ == '__main__':
    main()
