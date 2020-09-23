"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# 1. Implement the Queue class using an array as the underlying storage structure.
#    Make sure the Queue tests pass.

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        return self.storage

    def pop(self):
        if self.__len__() > 0:
            x = self.storage.pop()
            return x
        else:
            return None

# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Stack tests pass.

from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()

    def peek(self):
        return self.storage.head.get_value()            



stack = Stack()
stack.push(1)
stack.push(2)
print(len(stack))


# 3. What is the difference between using an array vs. a linked list when 
#    implementing a Queue?

'''
In order to insert or delete an element in/from an array, we need to move the order of the elements; it becomes 
an O(n) operation. However, it is easier to access the middle of an array than of a linked list because we access
elements using indices. 
Since we don't have indices while using linked list, both insertion and deletion operations take
the same amount of time - O(1) or O(c). Deletion from the beginning (head) of the linked list takes 
less or O(1) time than deleting from the tail, which takes longer or O(n) time. 

'''