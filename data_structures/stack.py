# We can implement a stack by an array or linkedlist.
from .linkedlist import LinkedList, Node

class StackList(LinkedList):
    def pop(self):

        if self.head is not None:
            to_pop = self.head
            self.head = to_pop.next
            return to_pop.data
        return None

    def peek(self):
        is self.head is None:
            return None
        return self.head.data

class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self, data):
        if len(self.stack) != 0:
            return self.stack.pop()
        return None

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
