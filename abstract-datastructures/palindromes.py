"""
Using two Queues and Stacks to check whether a given
word is a palindrome
"""
import pytest

class Stack(object):
    def __init__(self):
        self.values=[]
    def push(self, value):
        """
        Add a value to the top of the 
        stack
        """
        self.values.append(value)
    def pop(self):
        """
        Pop values
        """
        return self.values.pop()

class Queue(object):
    def __init__(self):
        self.values=[]
    def push(self, value):
        self.values.append(value)
    def pop(self):
        return self.values.pop(0)


stack = Stack()
stack.push(5)
stack.push(8)

print stack.values
print stack.pop()

queue = Queue()
queue.push(5)
queue.push(8)

print queue.values
print queue.pop()


class PalindromeChecker(object):
    """
    Checks if a word is a palindrome or not
    using two 
    """
    def __init__(self, word):
        self.word = word
        self.queue = Queue()
        self.stack = Stack()
    def check_palindrome(self):
        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)
        for i in range(len(self.word)):
            if self.queue.pop()!=self.stack.pop():
                return False
        return True


palindrome_checker = PalindromeChecker('radar')
print palindrome_checker.check_palindrome()
palindrome_checker_run = PalindromeChecker('run')
print palindrome_checker_run.check_palindrome()


