class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    
    # TODO: Add the __init__ method
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None
        self.__length = 0
        
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.__length += 1
        else:
            temp_node = self.head
            self.head = Node(value)
            self.head.next = temp_node
            self.__length += 1
    
    def pop(self):
        res = self.head.value
        self.head = self.head.next
        if not self.head.next:
            self.tail = self.head
        self.__length -= 1
        return res
            
    def size(self):
        return self.__length
    
    def is_empty(self):
        return bool(self.__length)
    