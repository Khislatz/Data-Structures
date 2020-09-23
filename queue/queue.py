"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# 1. Implement the Queue class using an array as the underlying storage structure.
#    Make sure the Queue tests pass.

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)
        return self.storage

    def dequeue(self):
        if self.__len__() > 0:
            x = self.storage.pop(0)
            return x
        else:
            return None

# 2. Re-implement the Queue class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Queue tests pass.

from linked_list import LinkedList


class Queue(LinkedList):
    
    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.add_to_tail(value)
        self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.remove_head()



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