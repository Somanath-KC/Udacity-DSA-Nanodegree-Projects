class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    def __repr__(self) -> str:
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out[:]
    
    def append(self, value):
        """
            Appends item at the end of linked-list.
        """
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
        self.__length += 1

    
    def prepend(self, value):
        """
            Prepends an item at the begining of linked-list.
        """
        
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            
        self.__length += 1
        
    
    def search(self, value):
        """
            Search's throught the linked list
            and returns the Node if it exits.
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            else:
                current_node = current_node.next
                
    
    def remove(self, value):
        """
            Remove the node from list with given value.
        """
        
        if self.head.value == value:
            self.head = self.head.next
            self.__length -= 1
        else:
            pre_node = self.head
            current_node = self.head.next
            
            while current_node:
                if current_node.value == value:
                    if current_node.next:
                        pre_node.next = current_node.next
                    else:
                        pre_node.next = None
                        self.tail = pre_node
                    self.__length -= 1
                    break
                else:
                    pre_node = current_node
                    current_node = current_node.next
    
    def pop(self):
        """
            Removes first node from linked list
            and returns that node .
        """
        if self.__length == 1:
            self.head = None
            self.tail = None
        else:
            current_value = self.head.value
            self.head = self.head.next
        
        self.__length -= 1
        return current_value
        
    
    def insert(self, value, pos):
        """
            Insert's value in specific postion.
            If pos is out of range insert at the end.
        """
        if pos == 0:
            self.prepend(value)
        elif pos < self.__length:
            counter = 1
            prev_node = self.head
            current_node = self.head.next
            while current_node:
                if counter == pos:
                    new_node = Node(value)
                    prev_node.next = new_node
                    new_node.next = current_node
                    self.__length += 1
                    break
                else:
                    prev_node = current_node
                    current_node = prev_node.next
                    counter += 1
        elif pos >= self.__length:
            self.append(value)
            
                
    def __len__(self):
        """
            Return's length of linked-list.
        """
        return self.__length