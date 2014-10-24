"""
A trial implementation of a stack
Learning from the book by M. Wahl (bt3gl on Github)

A stack is like a physical stack of books
"""

class Stack():
    def __init__(self):
        self.data=[]
    def pop(self):
        return self.data.pop()
    def push(self, item):
        return self.data.append(item)

"""
A simple test of the stack class
"""

fruits=Stack()
fruits.push("orange")
fruits.push("banana")
fruits.push("watermelon")
print fruits.pop()
