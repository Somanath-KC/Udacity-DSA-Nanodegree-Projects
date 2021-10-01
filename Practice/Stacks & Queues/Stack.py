"""
    Our goal will be to implement a Stack class that has the following behaviors:
        push - adds an item to the top of the stack
        pop - removes an item from the top of the stack (and returns the value of that item)
        size - returns the size of the stack
        top - returns the value of the item at the top of stack (without removing that item)
        is_empty - returns True if the stack is empty and False otherwise 
"""


class Stack:
    def __init__(self) -> None:
        self.arr = [0]*10
        self.next_index = 0
        self.num_elements = 0
        
    def _handle_stack_capacity_full(self):
        """
        Check if stack is overflowing.
        Increase the size if stack is full.

        Args:
            None
        """
        old_arr = self.arr[:]
        self.arr = old_arr + [0 for _ in range(10)]

    
    def push(self, value):
        """
        Add value on top of the stack.

        Args:
            value ([int]): [An Integer value to add on top of stack]
        """
        
        if self.num_elements >= len(self.arr):
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1
        
        
    def pop(self):
        """
        Removes the top most element in stack.

        Args: None
        """
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        res = self.arr[self.next_index]
        self.arr[self.next_index] = 0
        return res
        
        
    def size(self):
        """
        Return the size of stack. i.e Number of elements in Stack
        """
        return self.num_elements
    
    
    def is_empty(self):
        """
        Return Bool:
            True if stack is empty
            False if stack is not empty
        """
        return self.num_elements == 0 and self.next_index == 0
             