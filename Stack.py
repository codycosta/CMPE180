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
Main program

Solve the following problems using your Stack class:

Balanced Parentheses Checker
Write a function that checks if a string of brackets (e.g., "(()[]){}") is balanced.

Reverse a String Using a Stack
Write a function that uses a stack to reverse a given string.

Evaluate Postfix Expression
Implement a postfix (Reverse Polish Notation) expression evaluator, e.g., "3 4 + 2 * 7 /".

Undo Operation Simulation
Simulate an undo feature using a stack where actions are pushed and undone via pop.
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
    # if len(text) % 2:
    #     return False
    
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


def undo(actions: Stack):
    ''' undo an action by popping it from the stack '''
    
    if not actions.is_empty():
        actions.pop()


def postfix_interpreter(expression):
    ''' evaluates a math expression in reverse polish notation '''

    myStack = Stack()
    tokens = expression.split()

    # loop through expression
    for token in tokens:

        # if math operation
        if token in ['+', '-', '*', '/']:

            # if there's not 2 items to combine mathematically, end program
            if myStack.size() < 2:
                print('not enough arguments to evaluate')
                return
            
            # get the 2 items to combine mathematically
            a = float(myStack.pop())
            b = float(myStack.pop())

            # math
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                try:
                    result = a / b
                except ZeroDivisionError:
                    print(f'division by 0 occurred, ending program')
                    return None
                
            # add result to stack for next operation
            myStack.push(result)

        # add new expression item to stack
        else:
            try: 
                myStack.push(token)
            except ValueError:
                print(f'invalid token: {token}')
                return None
            
    # if end result is accompanied by an extra character in the expression
    if myStack.size() != 1:
        print('invalid expression, too many arguments')
        return None
    
    # else, only the result remains
    result = myStack.pop()
    return result                


            

def main():
    # reverse string
    print('Reverse a string:\n')
    text = 'Cody Costa'
    text_rev = reverse_string(text)
    print(text, text_rev)
    print('\n')

    # parentheses checker
    print('Parentheses Balance Checker:\n')
    print(parentheses_checker(r'(()[]){}'))
    print('\n')

    # undo action
    print('Undo Action:\n')
    log = Stack()
    actions = ['up', 'down', 'left', 'right']
    for i in actions:
        log.push(i)
    log.display()

    undo(log)
    log.display()
    print('\n')

    # postfix
    print('Reverse Polish Interpreter:\n')
    tests = ['3 4 + 2 * 7 /', '2 2 +', '0 1 /']
    for t in tests:
        result = postfix_interpreter(t)
        print(f'{t=}, {result=}')



if __name__ == '__main__':
    main()
